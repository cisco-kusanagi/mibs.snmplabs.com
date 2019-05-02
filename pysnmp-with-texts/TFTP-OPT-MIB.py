#
# PySNMP MIB module TFTP-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TFTP-OPT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:16:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, enterprises, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, Integer32, MibIdentifier, Counter32, ModuleIdentity, TimeTicks, NotificationType, iso, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "enterprises", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "Integer32", "MibIdentifier", "Counter32", "ModuleIdentity", "TimeTicks", "NotificationType", "iso", "Unsigned32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
codex = MibIdentifier((1, 3, 6, 1, 4, 1, 449))
cdxProductSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2))
cdx6500 = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1))
cdx6500Statistics = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3))
cdx6500StatTFTPGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3))
cdx6500Controls = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4))
cdx6500ContTFTP = MibIdentifier((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 2))
class DisplayString(OctetString):
    pass

cdx6500StatTFTPoperation = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100))).clone(namedValues=NamedValues(("configurationDownloadToCurrentBank", 1), ("configurationDownloadToAlternateBank", 2), ("configurationUploadFromCurrentBank", 3), ("configurationUploadFromAlternateBank", 4), ("softwareDownloadToCurrentBank", 5), ("softwareDownloadToAlternateBank", 6), ("configurationRestoreFromScript", 7), ("configurationRestoreToScript", 8), ("descriptionfileUpload", 9), ("nondefaultvalueUpload", 10), ("noOperation", 100)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500StatTFTPoperation.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500StatTFTPoperation.setDescription('Type and target of the last TFTP transfer or the one in progress, configuration download, configuration upload, software download, current or alternate bank. Configuration transfers will only be supported to/from the current bank at release 4.0.')
cdx6500StatTFTPIPaddress = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500StatTFTPIPaddress.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500StatTFTPIPaddress.setDescription('IP address of the remote TFTP application.')
cdx6500StatTFTPfilename = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500StatTFTPfilename.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500StatTFTPfilename.setDescription('File name used in the TFTP RRQ or WRQ message.')
cdx6500StatTFTPtimestamp = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500StatTFTPtimestamp.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500StatTFTPtimestamp.setDescription("Time of last operation. A null terminated string in the form `dd-mm-yyyy hh:mm:ss'. This will represent the starting time if the operation is in progress and the ending time if the operation has completed.")
cdx6500StatTFTPbytecount = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500StatTFTPbytecount.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500StatTFTPbytecount.setDescription('Total number of bytes transferred. This will represent a running total while the operation is in progress, and the final total after the operation has completed.')
cdx6500StatTFTPstatus = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500StatTFTPstatus.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500StatTFTPstatus.setDescription("Status of the latest configuration operation including an operation in progress. Possible status messages are: 'TFTP: No transfers since node last booted', 'TFTP: Transfer in progress' 'TFTP: Operation successful' 'TFTP: CMEM access failure' 'TFTP: Local transfer failure, <TFTP error message>, Error Code = <TFTP error code>' 'TFTP: Remote transfer failure, <TFTP error message>, Error Code = <TFTP error code>' 'TFTP: System failure' 'TFTP: UDP registration failure' 'TFTP: Flash erasure in progress' 'TFTP: Flash erasure failure' 'TFTP: Flash write failure' 'TFTP: Error in software image file' 'TFTP: Configuration script upload/download partial success' 'TFTP: Configuration script upload/download failure'")
cdx6500ContTFTPoperation = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100))).clone(namedValues=NamedValues(("configurationDownloadToCurrentBank", 1), ("configurationDownloadToAlternateBank", 2), ("configurationUploadFromCurrentBank", 3), ("configurationUploadFromAlternateBank", 4), ("softwareDownloadToCurrentBank", 5), ("softwareDownloadToAlternateBank", 6), ("configurationRestoreFromScript", 7), ("configurationRestoreToScript", 8), ("descriptionfileUpload", 9), ("nondefaultvalueUpload", 10), ("noOperation", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdx6500ContTFTPoperation.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500ContTFTPoperation.setDescription("Type and target of the TFTP transfer, configuration download, configuration upload, software download, current or alternate bank. Configuration transfers will only be supported to/from the current bank at release 4.0. Note that value 'noOperation' is not valid for the write operation.")
cdx6500ContTFTPIPaddress = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 2, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdx6500ContTFTPIPaddress.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500ContTFTPIPaddress.setDescription('IP address of the remote TFTP application.')
cdx6500ContTFTPfilename = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 2, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdx6500ContTFTPfilename.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500ContTFTPfilename.setDescription('File name to be used in the TFTP RRQ or WRQ message.')
cdx6500ContTFTPinitiateorder = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("start", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: cdx6500ContTFTPinitiateorder.setStatus('mandatory')
if mibBuilder.loadTexts: cdx6500ContTFTPinitiateorder.setDescription('Order to initiate the TFTP transfer.')
mibBuilder.exportSymbols("TFTP-OPT-MIB", codex=codex, cdx6500ContTFTPoperation=cdx6500ContTFTPoperation, cdx6500Controls=cdx6500Controls, cdx6500StatTFTPtimestamp=cdx6500StatTFTPtimestamp, cdxProductSpecific=cdxProductSpecific, cdx6500=cdx6500, cdx6500Statistics=cdx6500Statistics, cdx6500StatTFTPfilename=cdx6500StatTFTPfilename, cdx6500StatTFTPbytecount=cdx6500StatTFTPbytecount, cdx6500StatTFTPstatus=cdx6500StatTFTPstatus, cdx6500ContTFTPIPaddress=cdx6500ContTFTPIPaddress, cdx6500ContTFTPfilename=cdx6500ContTFTPfilename, cdx6500ContTFTP=cdx6500ContTFTP, cdx6500ContTFTPinitiateorder=cdx6500ContTFTPinitiateorder, cdx6500StatTFTPGroup=cdx6500StatTFTPGroup, DisplayString=DisplayString, cdx6500StatTFTPIPaddress=cdx6500StatTFTPIPaddress, cdx6500StatTFTPoperation=cdx6500StatTFTPoperation)
