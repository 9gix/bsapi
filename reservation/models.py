from django.db import models


class LoanRequestStatus:
    PENDING = 0
    APPROVED = 1
    REJECTED = -1


class LoanRequest(models.Model):

    _REQUEST_STATUS = (
        (LoanRequestStatus.PENDING, 'Waiting for owner approval'),
        (LoanRequestStatus.APPROVED, 'Loan Request approved'),
        (LoanRequestStatus.REJECTED, 'Loan Request rejected'),
    )

    owner_book = models.ForeignKey('ownership.UserBook')
    borrower_membership = models.ForeignKey('communities.Membership')

    status = models.IntegerField(max_length=1, choices=_REQUEST_STATUS,
            default=LoanRequestStatus.PENDING)

    def __str__(self):
        return "[{}] {} -requested- {}".format(
                self.get_status_display(),
                self.borrower_membership,
                self.owner_book)

    def approve(self):
        self.status = LoanRequestStatus.APPROVED
        return self.save()

    def reject(self):
        self.status = LoanRequestStatus.REJECTED
        return self.save()

    def isApproved(self):
        return self.status == LoanRequestStatus.APPROVED

    def isRejected(self):
        return self.status == LoanRequestStatus.REJECTED
