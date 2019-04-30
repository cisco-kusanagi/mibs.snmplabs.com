#
# PySNMP MIB module TFTP-OPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TFTP-OPT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:08:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, iso, Counter64, ModuleIdentity, Integer32, Counter32, NotificationType, ObjectIdentity, Gauge32, IpAddress, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "iso", "Counter64", "ModuleIdentity", "Integer32", "Counter32", "NotificationType", "ObjectIdentity", "Gauge32", "IpAddress", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits")
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
cdx6500StatTFTPIPaddress = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500StatTFTPIPaddress.setStatus('mandatory')
cdx6500StatTFTPfilename = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500StatTFTPfilename.setStatus('mandatory')
cdx6500StatTFTPtimestamp = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500StatTFTPtimestamp.setStatus('mandatory')
cdx6500StatTFTPbytecount = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500StatTFTPbytecount.setStatus('mandatory')
cdx6500StatTFTPstatus = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 3, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdx6500StatTFTPstatus.setStatus('mandatory')
cdx6500ContTFTPoperation = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100))).clone(namedValues=NamedValues(("configurationDownloadToCurrentBank", 1), ("configurationDownloadToAlternateBank", 2), ("configurationUploadFromCurrentBank", 3), ("configurationUploadFromAlternateBank", 4), ("softwareDownloadToCurrentBank", 5), ("softwareDownloadToAlternateBank", 6), ("configurationRestoreFromScript", 7), ("configurationRestoreToScript", 8), ("descriptionfileUpload", 9), ("nondefaultvalueUpload", 10), ("noOperation", 100)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdx6500ContTFTPoperation.setStatus('mandatory')
cdx6500ContTFTPIPaddress = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 2, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdx6500ContTFTPIPaddress.setStatus('mandatory')
cdx6500ContTFTPfilename = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 2, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdx6500ContTFTPfilename.setStatus('mandatory')
cdx6500ContTFTPinitiateorder = MibScalar((1, 3, 6, 1, 4, 1, 449, 2, 1, 4, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("start", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: cdx6500ContTFTPinitiateorder.setStatus('mandatory')
mibBuilder.exportSymbols("TFTP-OPT-MIB", DisplayString=DisplayString, cdx6500StatTFTPfilename=cdx6500StatTFTPfilename, cdx6500StatTFTPGroup=cdx6500StatTFTPGroup, cdx6500Controls=cdx6500Controls, cdx6500ContTFTPfilename=cdx6500ContTFTPfilename, codex=codex, cdx6500StatTFTPstatus=cdx6500StatTFTPstatus, cdxProductSpecific=cdxProductSpecific, cdx6500StatTFTPoperation=cdx6500StatTFTPoperation, cdx6500StatTFTPIPaddress=cdx6500StatTFTPIPaddress, cdx6500ContTFTPIPaddress=cdx6500ContTFTPIPaddress, cdx6500ContTFTPinitiateorder=cdx6500ContTFTPinitiateorder, cdx6500StatTFTPtimestamp=cdx6500StatTFTPtimestamp, cdx6500ContTFTP=cdx6500ContTFTP, cdx6500Statistics=cdx6500Statistics, cdx6500StatTFTPbytecount=cdx6500StatTFTPbytecount, cdx6500=cdx6500, cdx6500ContTFTPoperation=cdx6500ContTFTPoperation)
