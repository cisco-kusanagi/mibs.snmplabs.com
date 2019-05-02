#
# PySNMP MIB module ENTERASYS-SECURE-SHELL-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-SECURE-SHELL-SERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:04:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Integer32, NotificationType, IpAddress, Gauge32, Counter32, Counter64, ObjectIdentity, MibIdentifier, ModuleIdentity, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Integer32", "NotificationType", "IpAddress", "Gauge32", "Counter32", "Counter64", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "iso", "Unsigned32")
DateAndTime, DisplayString, TextualConvention, RowStatus, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention", "RowStatus", "StorageType")
etsysSecureShellServerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36))
etsysSecureShellServerMIB.setRevisions(('2003-02-12 17:14',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysSecureShellServerMIB.setRevisionsDescriptions(('The initial version of this MIB module.',))
if mibBuilder.loadTexts: etsysSecureShellServerMIB.setLastUpdated('200302121714Z')
if mibBuilder.loadTexts: etsysSecureShellServerMIB.setOrganization('Enterasys Networks, Inc')
if mibBuilder.loadTexts: etsysSecureShellServerMIB.setContactInfo('Postal: Enterasys Networks 35 Industrial Way, P.O. Box 5005 Rochester, NH 03867-0505 USA Phone: +1 603 332 9400 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: etsysSecureShellServerMIB.setDescription("This MIB module defines a portion of the SNMP enterprise MIBs under Enterasys Networks' enterprise OID pertaining to Secure Shell server management functionality, specifically for embedded systems. It provides configuration controls for Enterasys Networks' Secure Shell system management.")
etsysSecureShellServer = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1))
etsysSecureShellServerConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 1))
etsysSecureShellServerMac = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 2))
etsysSecureShellServerCipher = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 3))
etsysSecureShellServerHostKey = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4))
class SshCipherList(TextualConvention, Bits):
    description = 'The list of encryption ciphers that could be supported and enabled on the managed entities Secure Shell server.'
    status = 'current'
    namedValues = NamedValues(("triple-des-cbc", 0), ("twofish128-cbc", 1), ("blowfish-cbc", 2), ("cast128-cbc", 3), ("aes128-cbc", 4))

class SshMacList(TextualConvention, Bits):
    description = 'The list of MACs (Message Authentication Codes) that could be supported and enabled on the managed entities Secure Shell server.'
    status = 'current'
    namedValues = NamedValues(("hmac-md5", 0), ("hmac-md5-96", 1), ("hmac-sha1", 2), ("hmac-sha1-96", 3), ("hmac-ripemd160", 4))

class HexString(TextualConvention, OctetString):
    description = 'An OCTET-STRING with a suitable display hint.'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

etsysSecureShellServerAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("reinitialize", 3))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSecureShellServerAdminStatus.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerAdminStatus.setDescription("Controls the operation of the Secure Shell server. When enabled and the etsysSecureShellServerOperStatus object is 'operational' the Secure Shell server will accept connection requests and provide a secure CLI session for properly authenticated users. Setting this object to 'reinitialize' when it is in the 'enabled' state will cause the Secure Shell Server task to reinitialize itself and the value of this object will remain 'enabled'. Setting this object to 'reinitialize' from any other state will have no effect.")
etsysSecureShellServerOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("operational", 1), ("initializing", 2), ("nonOperational", 3))).clone('nonOperational')).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerOperStatus.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerOperStatus.setDescription('The current operational state of the Secure Shell Server.')
etsysSecureShellServerErrorStatus = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 1, 3), SnmpAdminString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerErrorStatus.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerErrorStatus.setDescription('A descriptive message indicating the reason for any failure of the Secure Shell Server to successfully transition into the operational state.')
etsysSecureShellServerAdminPort = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(22)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSecureShellServerAdminPort.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerAdminPort.setDescription('The TCP port number that the Secure Shell Server is should listen for connection requests on.')
etsysSecureShellServerOperPort = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerOperPort.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerOperPort.setDescription('The TCP port number that the Secure Shell Server is currently listening for connection requests on.')
etsysSecureShellServerSupportedMacs = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 2, 1), SshMacList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerSupportedMacs.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerSupportedMacs.setDescription('Specifies the MAC (Message Authentication Code) algorithms that are supported on this management entity.')
etsysSecureShellServerAdminMacs = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 2, 2), SshMacList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSecureShellServerAdminMacs.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerAdminMacs.setDescription('Specifies the MAC (Message Authentication Code) algorithms that the server should accept for use in data integrity verification. A re-initialization of the server may be required for this selection to take effect. By default managed entities SHOULD enable all of their supported MACs.')
etsysSecureShellServerOperMacs = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 2, 3), SshMacList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerOperMacs.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerOperMacs.setDescription('Specifies the MAC (Message Authentication Code) algorithms that the server is currently configured to accept for use in data integrity verification.')
etsysSecureShellServerSupportedCiphers = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 3, 1), SshCipherList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerSupportedCiphers.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerSupportedCiphers.setDescription('Specifies the ciphers that are supported on this management entity.')
etsysSecureShellServerAdminCiphers = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 3, 2), SshCipherList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSecureShellServerAdminCiphers.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerAdminCiphers.setDescription('The cipher(s) that the server should accept for use in encrypting secure sessions. A re-initialization of the server may be required for this selection to take effect. By default managed entities SHOULD enable all of their supported ciphers.')
etsysSecureShellServerOperCiphers = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 3, 3), SshCipherList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerOperCiphers.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerOperCiphers.setDescription('Specifies the cipher(s) that the server is currently configured to accept for use in encrypting all sessions.')
etsysSecureShellServerHostKeyTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1), )
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyTable.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyTable.setDescription('A table that contains per public/private host key pair information.')
etsysSecureShellServerHostKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1), ).setIndexNames((0, "ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyType"), (0, "ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeySize"))
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyEntry.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyEntry.setDescription('A list information about a particular public/private host key pair.')
etsysSecureShellServerHostKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sshDss", 1), ("sshRsa", 2))))
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyType.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyType.setDescription('The type of the public/private host key pair represented by this conceptual row.')
etsysSecureShellServerHostKeySize = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("bits512", 1), ("bits768", 2), ("bits1024", 3), ("bits2048", 4))))
if mibBuilder.loadTexts: etsysSecureShellServerHostKeySize.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerHostKeySize.setDescription('The size of the public/private host key pair represented by this conceptual row.')
etsysSecureShellServerHostKeyDate = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyDate.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyDate.setDescription('The date and time the public/private host key pair that is represented by this row, and is currently operational, was generated.')
etsysSecureShellServerHostKeyOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 4), Bits().clone(namedValues=NamedValues(("initializing", 0), ("operational", 1), ("completed", 2), ("pending", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyOperStatus.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyOperStatus.setDescription('The status of this public/private host key pair. The meaning of the values are as follows: initializing (0) Indicates that a new host key pair, of the size and type specified by this row, is being generated. operational (1) Indicates that the host key pair described by this row is currently operational. completed (2) Indicates that the host key pair has been successfully initialized or reinitialized. pending (3) Indicates that the new host key pair will not become operational until the server is reinitialized. failed (4) Indicates that the host key pair generation operation has failed.')
etsysSecureShellServerHostKeyAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noOp", 1), ("reinitialize", 2))).clone('noOp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyAdminStatus.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyAdminStatus.setDescription('Reinitializing the private/public host key pair can be compute intensive. Writing reinitialize(2) to this object while the etsysSecureShellServerHostOperStatus object indicates that a host key initialization is currently in progress has no affect. The meaning of the values are as follows: noOp (1) This object always returns noOp(1) on a read. A write of noOp(1) has no affect. reinitialize (2) Writing reinitialize(2) causes the managed entity to generate a new host key pair of the size and type specified by this row.')
etsysSecureShellServerHostKeyFingerprint = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 6), HexString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyFingerprint.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyFingerprint.setDescription('The RSA fingerprint of the public part of the host key pair. This value can be used with the SSH client to verify, on the initial connection, that the Secure Shell server responding to the request is the server running on the managed entity. This is the fingerprint of the operational host key pair. If the key pair represented by this row is not operational then sixteen null octets MUST be returned.')
etsysSecureShellServerHostKeyErrorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 7), SnmpAdminString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyErrorStatus.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyErrorStatus.setDescription('This is a descriptive error message about any failure to generate an initial public/private host key pair, or to reinitialize the key pair for this row. This would include messages to the effect of exceeding the number of key pairs supported by this managed entity. This message reverts back to its default value when the etsysSecureShellServerHostAdminStatus object is set to reinitialize(2).')
etsysSecureShellServerHostKeyStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 8), StorageType().clone('nonVolatile')).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyStorageType.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyStorageType.setDescription("The storage type for this conceptual row. Managed entities that do not support configurable host keys MUST define this row as 'permanent' and need not allow write-access to the RowStatus object in the row. All user created rows MUST have the default value, nonVolatile.")
etsysSecureShellServerHostKeyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyRowStatus.setReference('RFC2579 (Textual Conventions for SMIv2)')
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyRowStatus.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyRowStatus.setDescription('This object manages the creation and deletion this entry. active - Indicates that the host key pair represented by this row is available for use by the Secure Shell Server to the extent indicated by the status objects in this row. Transitions to this state will cause a a new host key pair to be generated by the managed entity. notInService - Indicates that this entry exists in the agent but is unavailable for use. State transitions from the active(1) state to the notInService(2) state will cause the host key pair represented by this row to be deleted. notReady - Should not be possible. createAndWait - A new entry will be created in this table for the specified host key pair and the new entry will transition to the notInService(2) state. No key pair will be generated. createAndGo - A new entry will be created in this table for the specified host key pair and the new entry will transition to the active(1) state. destroy - Deletes this row and any host key pair that may be associated with it.')
etsysSecureShellServerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 2))
etsysSecureShellServerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 2, 1))
etsysSecureShellServerCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 2, 2))
etsysSecureShellServerConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 2, 1, 1)).setObjects(("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerAdminStatus"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerOperStatus"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerAdminPort"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerOperPort"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerSupportedMacs"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerAdminMacs"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerOperMacs"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerSupportedCiphers"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerAdminCiphers"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerOperCiphers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSecureShellServerConfigGroup = etsysSecureShellServerConfigGroup.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerConfigGroup.setDescription('A collection of objects providing basic SSH server configuration on a managed entity.')
etsysSecureShellServerHostKeyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 2, 1, 2)).setObjects(("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyDate"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyOperStatus"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyAdminStatus"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyFingerprint"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyErrorStatus"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyStorageType"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSecureShellServerHostKeyGroup = etsysSecureShellServerHostKeyGroup.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyGroup.setDescription('A collection of objects providing basic SSH server host key management on a managed entity.')
etsysSecureShellServerCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 2, 2, 1)).setObjects(("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerConfigGroup"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSecureShellServerCompliance = etsysSecureShellServerCompliance.setStatus('current')
if mibBuilder.loadTexts: etsysSecureShellServerCompliance.setDescription('The compliance statement for devices that support the Enterasys Secure Shell (SSH) MIB.')
mibBuilder.exportSymbols("ENTERASYS-SECURE-SHELL-SERVER-MIB", etsysSecureShellServer=etsysSecureShellServer, etsysSecureShellServerHostKeySize=etsysSecureShellServerHostKeySize, etsysSecureShellServerHostKeyType=etsysSecureShellServerHostKeyType, etsysSecureShellServerHostKeyStorageType=etsysSecureShellServerHostKeyStorageType, etsysSecureShellServerGroups=etsysSecureShellServerGroups, etsysSecureShellServerHostKeyDate=etsysSecureShellServerHostKeyDate, SshCipherList=SshCipherList, etsysSecureShellServerMIB=etsysSecureShellServerMIB, etsysSecureShellServerOperMacs=etsysSecureShellServerOperMacs, etsysSecureShellServerConfig=etsysSecureShellServerConfig, etsysSecureShellServerAdminMacs=etsysSecureShellServerAdminMacs, HexString=HexString, etsysSecureShellServerSupportedMacs=etsysSecureShellServerSupportedMacs, etsysSecureShellServerConfigGroup=etsysSecureShellServerConfigGroup, etsysSecureShellServerConformance=etsysSecureShellServerConformance, etsysSecureShellServerCompliance=etsysSecureShellServerCompliance, etsysSecureShellServerErrorStatus=etsysSecureShellServerErrorStatus, etsysSecureShellServerOperStatus=etsysSecureShellServerOperStatus, etsysSecureShellServerAdminStatus=etsysSecureShellServerAdminStatus, etsysSecureShellServerSupportedCiphers=etsysSecureShellServerSupportedCiphers, etsysSecureShellServerHostKeyRowStatus=etsysSecureShellServerHostKeyRowStatus, etsysSecureShellServerOperCiphers=etsysSecureShellServerOperCiphers, etsysSecureShellServerOperPort=etsysSecureShellServerOperPort, etsysSecureShellServerMac=etsysSecureShellServerMac, etsysSecureShellServerHostKeyAdminStatus=etsysSecureShellServerHostKeyAdminStatus, etsysSecureShellServerHostKey=etsysSecureShellServerHostKey, etsysSecureShellServerAdminPort=etsysSecureShellServerAdminPort, etsysSecureShellServerCompliances=etsysSecureShellServerCompliances, etsysSecureShellServerHostKeyFingerprint=etsysSecureShellServerHostKeyFingerprint, etsysSecureShellServerAdminCiphers=etsysSecureShellServerAdminCiphers, etsysSecureShellServerHostKeyGroup=etsysSecureShellServerHostKeyGroup, etsysSecureShellServerCipher=etsysSecureShellServerCipher, etsysSecureShellServerHostKeyOperStatus=etsysSecureShellServerHostKeyOperStatus, etsysSecureShellServerHostKeyErrorStatus=etsysSecureShellServerHostKeyErrorStatus, etsysSecureShellServerHostKeyTable=etsysSecureShellServerHostKeyTable, etsysSecureShellServerHostKeyEntry=etsysSecureShellServerHostKeyEntry, PYSNMP_MODULE_ID=etsysSecureShellServerMIB, SshMacList=SshMacList)
