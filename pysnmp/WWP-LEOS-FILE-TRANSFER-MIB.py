#
# PySNMP MIB module WWP-LEOS-FILE-TRANSFER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-LEOS-FILE-TRANSFER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:31:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, MibIdentifier, Counter32, Counter64, Bits, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, IpAddress, Unsigned32, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "Counter32", "Counter64", "Bits", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "IpAddress", "Unsigned32", "NotificationType", "ModuleIdentity")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
wwpModulesLeos, = mibBuilder.importSymbols("WWP-SMI", "wwpModulesLeos")
wwpLeosFileTransferMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23))
wwpLeosFileTransferMIB.setRevisions(('2012-03-22 00:00', '2001-04-03 17:00',))
if mibBuilder.loadTexts: wwpLeosFileTransferMIB.setLastUpdated('201203220000Z')
if mibBuilder.loadTexts: wwpLeosFileTransferMIB.setOrganization('Ciena, Inc')
wwpLeosFileTransferMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1))
wwpLeosFileTransfer = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1))
wwpLeosFileTransferMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 2))
wwpLeosFiletransferMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 2, 0))
wwpLeosFileTransferMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 3))
wwpLeosFileTransferMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 3, 1))
wwpLeosFileTransferMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 3, 2))
class FileTransferState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("idle", 1), ("sending", 2), ("receiving", 3), ("transferComplete", 4), ("failed", 5))

class FileTransferFailCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("noStatus", 1), ("timeout", 2), ("networkError", 3), ("noSpace", 4), ("invalidFileName", 5), ("commandCompleted", 6), ("internalError", 7), ("commandFileParseError", 8))

wwpLeosFTransferOp = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("sendFile", 1), ("getFile", 2), ("getCmdFile", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosFTransferOp.setStatus('current')
wwpLeosFTransferServerAddr = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 2), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosFTransferServerAddr.setStatus('current')
wwpLeosFTransferRemoteFilename = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosFTransferRemoteFilename.setStatus('current')
wwpLeosFTransferLocalFilename = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosFTransferLocalFilename.setStatus('current')
wwpLeosFTransferActivate = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosFTransferActivate.setStatus('current')
wwpLeosFTransferNotifOnCompletion = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosFTransferNotifOnCompletion.setStatus('current')
wwpLeosFTransferStatus = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 7), FileTransferState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosFTransferStatus.setStatus('current')
wwpLeosFTransferFailCause = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 8), FileTransferFailCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosFTransferFailCause.setStatus('current')
wwpLeosFTransferNotificationStatus = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24))).clone(namedValues=NamedValues(("downloadSuccess", 0), ("tftpServerNotFound", 1), ("couldNotGetFile", 2), ("cmdFileParseError", 3), ("internalFilesystemError", 4), ("inValidFileContents", 5), ("flashOffline", 6), ("noStatus", 7), ("putSuccessful", 8), ("couldNotPutFile", 9), ("badFileCrc", 10), ("allFilesSkipped", 11), ("fileAlreadyExist", 12), ("fileGetError", 13), ("filePutError", 14), ("fileSystemError", 15), ("fileContentsInvalid", 16), ("serverIpAddrInvalid", 18), ("filePathInvalid", 19), ("fileNameInvalid", 20), ("sourceNotFound", 21), ("fileNameNeeded", 22), ("notEnoughSpace", 23), ("internalError", 24)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosFTransferNotificationStatus.setStatus('current')
wwpLeosFTransferNotificationInfo = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosFTransferNotificationInfo.setStatus('current')
wwpLeosFTransferServerInetAddrType = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 11), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosFTransferServerInetAddrType.setStatus('current')
wwpLeosFTransferServerInetAddr = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 12), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosFTransferServerInetAddr.setStatus('current')
wwpLeosFTransferCompletion = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 2, 0, 1)).setObjects(("WWP-LEOS-FILE-TRANSFER-MIB", "wwpLeosFTransferRemoteFilename"), ("WWP-LEOS-FILE-TRANSFER-MIB", "wwpLeosFTransferLocalFilename"), ("WWP-LEOS-FILE-TRANSFER-MIB", "wwpLeosFTransferNotificationStatus"), ("WWP-LEOS-FILE-TRANSFER-MIB", "wwpLeosFTransferNotificationInfo"))
if mibBuilder.loadTexts: wwpLeosFTransferCompletion.setStatus('current')
wwpLeosFileTransferCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 3, 1, 1)).setObjects(("WWP-LEOS-FILE-TRANSFER-MIB", "wwpLeosFileTransferIPv6Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wwpLeosFileTransferCompliance = wwpLeosFileTransferCompliance.setStatus('current')
wwpLeosFileTransferIPv6Group = ObjectGroup((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 3, 2, 1)).setObjects(("WWP-LEOS-FILE-TRANSFER-MIB", "wwpLeosFTransferServerInetAddrType"), ("WWP-LEOS-FILE-TRANSFER-MIB", "wwpLeosFTransferServerInetAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wwpLeosFileTransferIPv6Group = wwpLeosFileTransferIPv6Group.setStatus('current')
mibBuilder.exportSymbols("WWP-LEOS-FILE-TRANSFER-MIB", wwpLeosFileTransfer=wwpLeosFileTransfer, wwpLeosFTransferRemoteFilename=wwpLeosFTransferRemoteFilename, wwpLeosFiletransferMIBNotifications=wwpLeosFiletransferMIBNotifications, FileTransferFailCause=FileTransferFailCause, wwpLeosFTransferServerInetAddrType=wwpLeosFTransferServerInetAddrType, wwpLeosFileTransferMIBNotificationPrefix=wwpLeosFileTransferMIBNotificationPrefix, wwpLeosFTransferActivate=wwpLeosFTransferActivate, wwpLeosFTransferServerAddr=wwpLeosFTransferServerAddr, wwpLeosFileTransferCompliance=wwpLeosFileTransferCompliance, wwpLeosFTransferNotifOnCompletion=wwpLeosFTransferNotifOnCompletion, FileTransferState=FileTransferState, wwpLeosFileTransferMIB=wwpLeosFileTransferMIB, PYSNMP_MODULE_ID=wwpLeosFileTransferMIB, wwpLeosFTransferServerInetAddr=wwpLeosFTransferServerInetAddr, wwpLeosFTransferStatus=wwpLeosFTransferStatus, wwpLeosFTransferCompletion=wwpLeosFTransferCompletion, wwpLeosFTransferFailCause=wwpLeosFTransferFailCause, wwpLeosFileTransferMIBGroups=wwpLeosFileTransferMIBGroups, wwpLeosFileTransferIPv6Group=wwpLeosFileTransferIPv6Group, wwpLeosFileTransferMIBConformance=wwpLeosFileTransferMIBConformance, wwpLeosFTransferNotificationInfo=wwpLeosFTransferNotificationInfo, wwpLeosFTransferOp=wwpLeosFTransferOp, wwpLeosFileTransferMIBCompliances=wwpLeosFileTransferMIBCompliances, wwpLeosFTransferNotificationStatus=wwpLeosFTransferNotificationStatus, wwpLeosFileTransferMIBObjects=wwpLeosFileTransferMIBObjects, wwpLeosFTransferLocalFilename=wwpLeosFTransferLocalFilename)
