#
# PySNMP MIB module WWP-LEOS-FILE-TRANSFER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-LEOS-FILE-TRANSFER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:37:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, NotificationType, Counter32, IpAddress, Integer32, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "NotificationType", "Counter32", "IpAddress", "Integer32", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "Unsigned32", "Bits")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
wwpModulesLeos, = mibBuilder.importSymbols("WWP-SMI", "wwpModulesLeos")
wwpLeosFileTransferMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23))
wwpLeosFileTransferMIB.setRevisions(('2012-03-22 00:00', '2001-04-03 17:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wwpLeosFileTransferMIB.setRevisionsDescriptions(('Added new MIB OIDs to support protocol version independent of Inet Addressing. wwpLeosFTransferServerInetAddr and wwpLeosFTransferServerInetAddrType are added.', 'Initial creation.',))
if mibBuilder.loadTexts: wwpLeosFileTransferMIB.setLastUpdated('201203220000Z')
if mibBuilder.loadTexts: wwpLeosFileTransferMIB.setOrganization('Ciena, Inc')
if mibBuilder.loadTexts: wwpLeosFileTransferMIB.setContactInfo(' Mib Meister 115 North Sullivan Road Spokane Valley, WA 99037 USA Phone: +1 509 242 9000 Email: support@ciena.com')
if mibBuilder.loadTexts: wwpLeosFileTransferMIB.setDescription('The MIB module for the WWP TFTP Operation to download a file.')
wwpLeosFileTransferMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1))
wwpLeosFileTransfer = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1))
wwpLeosFileTransferMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 2))
wwpLeosFiletransferMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 2, 0))
wwpLeosFileTransferMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 3))
wwpLeosFileTransferMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 3, 1))
wwpLeosFileTransferMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 3, 2))
class FileTransferState(TextualConvention, Integer32):
    description = 'The state of a File transfer operation. The description of each state is given below: idle: No file transfer operation is in place. sending: this state signifies that the file is being sent to the TFTP server. receiving: this state signifies that the file is being received from the TFTP server. transferComplete: the state when a file transfer request is successfully completed. failed: the file transfer request was unsuccesful. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("idle", 1), ("sending", 2), ("receiving", 3), ("transferComplete", 4), ("failed", 5))

class FileTransferFailCause(TextualConvention, Integer32):
    description = 'The reason a File transfer request failed.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("noStatus", 1), ("timeout", 2), ("networkError", 3), ("noSpace", 4), ("invalidFileName", 5), ("commandCompleted", 6), ("internalError", 7), ("commandFileParseError", 8))

wwpLeosFTransferOp = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("sendFile", 1), ("getFile", 2), ("getCmdFile", 3))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosFTransferOp.setStatus('current')
if mibBuilder.loadTexts: wwpLeosFTransferOp.setDescription('Used to transfer file(s) between a TFTP server (remote) and the device(local). All transfers are binary. There are three types of file transfers: sendFile sends a file to the host TFTP server. getFile receives a file from the host server. getCmdFile gets the specified file from the host and parses that file for additional operations to be performed. This is the mechanism used to upgrade the device with new software.')
wwpLeosFTransferServerAddr = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 2), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosFTransferServerAddr.setStatus('current')
if mibBuilder.loadTexts: wwpLeosFTransferServerAddr.setDescription('The IP address of the TFTP server from (or to) which to transfer the file.Address must be a unicast address that is reachable from the agent and no firewalls or ACLs preventing TFTP datagrams from being transferred. wwpLeosFTransferServerInetAddr cannot be set at the same time. This OID will be set to 0.0.0.0 when the server has an IPv6 address, which is shown in the wwpLeosFTransferServerInetAddr and the wwpLeosDnsServerInetAddrType is set to ipv6. For a server with an IPv4 address, the ip address will be shown in this OID and the wwpLeosFTransferServerInetAddr with the wwpLeosDnsServerInetAddrType set to ipv4.')
wwpLeosFTransferRemoteFilename = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosFTransferRemoteFilename.setStatus('current')
if mibBuilder.loadTexts: wwpLeosFTransferRemoteFilename.setDescription('The file name (including the path, if applicable) to be retrieved from the TFTP server. If the switch/device is downloading a file, then this should be the name of the file on the remote server. Length of filename string must not exceed 64 alpha-numeric characters, no spaces in filenames.')
wwpLeosFTransferLocalFilename = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosFTransferLocalFilename.setStatus('current')
if mibBuilder.loadTexts: wwpLeosFTransferLocalFilename.setDescription('The file name (including the path, if applicable) to be written to. If the switch/device is downloading a file, then this should be the name of the file on the switch/device. Length of filename string must not exceed 64 alpha-numeric characters, no spaces in filenames. By default it will have the same value as of wwpLeosFTransferRemoteFilename.')
wwpLeosFTransferActivate = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosFTransferActivate.setStatus('current')
if mibBuilder.loadTexts: wwpLeosFTransferActivate.setDescription("Activate the file transfer operation with a value of True(1). The object will return to 'false' once the file transfer is completed. Poll wwpLeosFTransferStatus for current status. Default value is False. wwpLeosFTransferRemoteFileName, wwpLeosFTransferServerAddress and wwpLeosFTransferOp must be valid prior to setting this object to True.")
wwpLeosFTransferNotifOnCompletion = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosFTransferNotifOnCompletion.setStatus('current')
if mibBuilder.loadTexts: wwpLeosFTransferNotifOnCompletion.setDescription('Specifies whether or not a wwpLeosFTransferCompletion notification should be issued on completion of the TFTP transfer. If such a notification is desired, it is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the notification to be delivered.')
wwpLeosFTransferStatus = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 7), FileTransferState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosFTransferStatus.setStatus('current')
if mibBuilder.loadTexts: wwpLeosFTransferStatus.setDescription("Specifies the state of this file transfer request. If no file transfer request is being processed, then the wwpLeosFTransferStatus should be 'idle'.")
wwpLeosFTransferFailCause = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 8), FileTransferFailCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosFTransferFailCause.setStatus('current')
if mibBuilder.loadTexts: wwpLeosFTransferFailCause.setDescription("The reason why the file transfer operation failed. If no file transfer request is being processed, then the wwpLeosFTransferFileCause should be 'noStatus'.")
wwpLeosFTransferNotificationStatus = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24))).clone(namedValues=NamedValues(("downloadSuccess", 0), ("tftpServerNotFound", 1), ("couldNotGetFile", 2), ("cmdFileParseError", 3), ("internalFilesystemError", 4), ("inValidFileContents", 5), ("flashOffline", 6), ("noStatus", 7), ("putSuccessful", 8), ("couldNotPutFile", 9), ("badFileCrc", 10), ("allFilesSkipped", 11), ("fileAlreadyExist", 12), ("fileGetError", 13), ("filePutError", 14), ("fileSystemError", 15), ("fileContentsInvalid", 16), ("serverIpAddrInvalid", 18), ("filePathInvalid", 19), ("fileNameInvalid", 20), ("sourceNotFound", 21), ("fileNameNeeded", 22), ("notEnoughSpace", 23), ("internalError", 24)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosFTransferNotificationStatus.setStatus('current')
if mibBuilder.loadTexts: wwpLeosFTransferNotificationStatus.setDescription('The status of the file transfer which is to be reported via the FileTransfer Notification.')
wwpLeosFTransferNotificationInfo = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosFTransferNotificationInfo.setStatus('current')
if mibBuilder.loadTexts: wwpLeosFTransferNotificationInfo.setDescription('The string explaining the error code in detail or the additional info for the file transfer completion.')
wwpLeosFTransferServerInetAddrType = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 11), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosFTransferServerInetAddrType.setStatus('current')
if mibBuilder.loadTexts: wwpLeosFTransferServerInetAddrType.setDescription('The Inet address type of the TFTP server from (or to) which to transfer the file. Used in conjunction with wwpLeosFTransferServerInetAddr. When set to : ipv4: wwpLeosFTransferServerInetAddr should be compliant with InetAddressIPv4 from RFC 4001 ipv6: wwpLeosFTransferServerInetAddr should be compliant with InetAddressIPv6 from RFC 4001')
wwpLeosFTransferServerInetAddr = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 1, 1, 12), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosFTransferServerInetAddr.setStatus('current')
if mibBuilder.loadTexts: wwpLeosFTransferServerInetAddr.setDescription('The Inet address of the TFTP server from (or to) which to transfer the file. Address must be a unicast address that is reachable from the agent and no firewalls or ACLs preventing TFTP datagrams from being transferred. This OID must be used in conjuction with wwpLeosFTransferServerInetAddrType. The InetAddress set here should be compliant with rfc 4001 InetAddressType. When this OID is set, wwpLeosFTransferServerAddr is set ot 0.0.0.0.')
wwpLeosFTransferCompletion = NotificationType((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 2, 0, 1)).setObjects(("WWP-LEOS-FILE-TRANSFER-MIB", "wwpLeosFTransferRemoteFilename"), ("WWP-LEOS-FILE-TRANSFER-MIB", "wwpLeosFTransferLocalFilename"), ("WWP-LEOS-FILE-TRANSFER-MIB", "wwpLeosFTransferNotificationStatus"), ("WWP-LEOS-FILE-TRANSFER-MIB", "wwpLeosFTransferNotificationInfo"))
if mibBuilder.loadTexts: wwpLeosFTransferCompletion.setStatus('current')
if mibBuilder.loadTexts: wwpLeosFTransferCompletion.setDescription('A wwpLeosFTransferCompletion notification is sent at the completion of a file transfer request.')
wwpLeosFileTransferCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 3, 1, 1)).setObjects(("WWP-LEOS-FILE-TRANSFER-MIB", "wwpLeosFileTransferIPv6Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wwpLeosFileTransferCompliance = wwpLeosFileTransferCompliance.setStatus('current')
if mibBuilder.loadTexts: wwpLeosFileTransferCompliance.setDescription('The compliance statement of the wwpLeosFileTransfer MIB.')
wwpLeosFileTransferIPv6Group = ObjectGroup((1, 3, 6, 1, 4, 1, 6141, 2, 60, 23, 3, 2, 1)).setObjects(("WWP-LEOS-FILE-TRANSFER-MIB", "wwpLeosFTransferServerInetAddrType"), ("WWP-LEOS-FILE-TRANSFER-MIB", "wwpLeosFTransferServerInetAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    wwpLeosFileTransferIPv6Group = wwpLeosFileTransferIPv6Group.setStatus('current')
if mibBuilder.loadTexts: wwpLeosFileTransferIPv6Group.setDescription('File transfer objects for IPv6 address.')
mibBuilder.exportSymbols("WWP-LEOS-FILE-TRANSFER-MIB", wwpLeosFiletransferMIBNotifications=wwpLeosFiletransferMIBNotifications, wwpLeosFTransferNotificationStatus=wwpLeosFTransferNotificationStatus, wwpLeosFileTransferMIBObjects=wwpLeosFileTransferMIBObjects, wwpLeosFTransferOp=wwpLeosFTransferOp, wwpLeosFTransferServerInetAddrType=wwpLeosFTransferServerInetAddrType, FileTransferState=FileTransferState, FileTransferFailCause=FileTransferFailCause, wwpLeosFTransferServerInetAddr=wwpLeosFTransferServerInetAddr, wwpLeosFileTransferIPv6Group=wwpLeosFileTransferIPv6Group, PYSNMP_MODULE_ID=wwpLeosFileTransferMIB, wwpLeosFTransferActivate=wwpLeosFTransferActivate, wwpLeosFileTransferMIBConformance=wwpLeosFileTransferMIBConformance, wwpLeosFileTransferMIBGroups=wwpLeosFileTransferMIBGroups, wwpLeosFileTransferCompliance=wwpLeosFileTransferCompliance, wwpLeosFTransferFailCause=wwpLeosFTransferFailCause, wwpLeosFTransferLocalFilename=wwpLeosFTransferLocalFilename, wwpLeosFTransferCompletion=wwpLeosFTransferCompletion, wwpLeosFTransferNotificationInfo=wwpLeosFTransferNotificationInfo, wwpLeosFTransferRemoteFilename=wwpLeosFTransferRemoteFilename, wwpLeosFileTransferMIB=wwpLeosFileTransferMIB, wwpLeosFTransferStatus=wwpLeosFTransferStatus, wwpLeosFTransferServerAddr=wwpLeosFTransferServerAddr, wwpLeosFileTransferMIBNotificationPrefix=wwpLeosFileTransferMIBNotificationPrefix, wwpLeosFileTransferMIBCompliances=wwpLeosFileTransferMIBCompliances, wwpLeosFileTransfer=wwpLeosFileTransfer, wwpLeosFTransferNotifOnCompletion=wwpLeosFTransferNotifOnCompletion)
