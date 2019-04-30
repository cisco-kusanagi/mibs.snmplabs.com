#
# PySNMP MIB module ENTERASYS-SECURE-SHELL-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-SECURE-SHELL-SERVER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:50:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, Counter64, Gauge32, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, iso, MibIdentifier, Integer32, TimeTicks, ObjectIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Gauge32", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "iso", "MibIdentifier", "Integer32", "TimeTicks", "ObjectIdentity", "Counter32")
DisplayString, TextualConvention, DateAndTime, StorageType, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime", "StorageType", "RowStatus")
etsysSecureShellServerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36))
etsysSecureShellServerMIB.setRevisions(('2003-02-12 17:14',))
if mibBuilder.loadTexts: etsysSecureShellServerMIB.setLastUpdated('200302121714Z')
if mibBuilder.loadTexts: etsysSecureShellServerMIB.setOrganization('Enterasys Networks, Inc')
etsysSecureShellServer = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1))
etsysSecureShellServerConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 1))
etsysSecureShellServerMac = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 2))
etsysSecureShellServerCipher = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 3))
etsysSecureShellServerHostKey = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4))
class SshCipherList(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("triple-des-cbc", 0), ("twofish128-cbc", 1), ("blowfish-cbc", 2), ("cast128-cbc", 3), ("aes128-cbc", 4))

class SshMacList(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("hmac-md5", 0), ("hmac-md5-96", 1), ("hmac-sha1", 2), ("hmac-sha1-96", 3), ("hmac-ripemd160", 4))

class HexString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

etsysSecureShellServerAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("reinitialize", 3))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSecureShellServerAdminStatus.setStatus('current')
etsysSecureShellServerOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("operational", 1), ("initializing", 2), ("nonOperational", 3))).clone('nonOperational')).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerOperStatus.setStatus('current')
etsysSecureShellServerErrorStatus = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 1, 3), SnmpAdminString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerErrorStatus.setStatus('current')
etsysSecureShellServerAdminPort = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(22)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSecureShellServerAdminPort.setStatus('current')
etsysSecureShellServerOperPort = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerOperPort.setStatus('current')
etsysSecureShellServerSupportedMacs = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 2, 1), SshMacList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerSupportedMacs.setStatus('current')
etsysSecureShellServerAdminMacs = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 2, 2), SshMacList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSecureShellServerAdminMacs.setStatus('current')
etsysSecureShellServerOperMacs = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 2, 3), SshMacList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerOperMacs.setStatus('current')
etsysSecureShellServerSupportedCiphers = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 3, 1), SshCipherList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerSupportedCiphers.setStatus('current')
etsysSecureShellServerAdminCiphers = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 3, 2), SshCipherList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSecureShellServerAdminCiphers.setStatus('current')
etsysSecureShellServerOperCiphers = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 3, 3), SshCipherList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerOperCiphers.setStatus('current')
etsysSecureShellServerHostKeyTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1), )
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyTable.setStatus('current')
etsysSecureShellServerHostKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1), ).setIndexNames((0, "ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyType"), (0, "ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeySize"))
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyEntry.setStatus('current')
etsysSecureShellServerHostKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sshDss", 1), ("sshRsa", 2))))
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyType.setStatus('current')
etsysSecureShellServerHostKeySize = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("bits512", 1), ("bits768", 2), ("bits1024", 3), ("bits2048", 4))))
if mibBuilder.loadTexts: etsysSecureShellServerHostKeySize.setStatus('current')
etsysSecureShellServerHostKeyDate = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyDate.setStatus('current')
etsysSecureShellServerHostKeyOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 4), Bits().clone(namedValues=NamedValues(("initializing", 0), ("operational", 1), ("completed", 2), ("pending", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyOperStatus.setStatus('current')
etsysSecureShellServerHostKeyAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noOp", 1), ("reinitialize", 2))).clone('noOp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyAdminStatus.setStatus('current')
etsysSecureShellServerHostKeyFingerprint = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 6), HexString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyFingerprint.setStatus('current')
etsysSecureShellServerHostKeyErrorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 7), SnmpAdminString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyErrorStatus.setStatus('current')
etsysSecureShellServerHostKeyStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 8), StorageType().clone('nonVolatile')).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyStorageType.setStatus('current')
etsysSecureShellServerHostKeyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 1, 4, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysSecureShellServerHostKeyRowStatus.setStatus('current')
etsysSecureShellServerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 2))
etsysSecureShellServerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 2, 1))
etsysSecureShellServerCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 2, 2))
etsysSecureShellServerConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 2, 1, 1)).setObjects(("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerAdminStatus"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerOperStatus"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerAdminPort"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerOperPort"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerSupportedMacs"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerAdminMacs"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerOperMacs"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerSupportedCiphers"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerAdminCiphers"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerOperCiphers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSecureShellServerConfigGroup = etsysSecureShellServerConfigGroup.setStatus('current')
etsysSecureShellServerHostKeyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 2, 1, 2)).setObjects(("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyDate"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyOperStatus"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyAdminStatus"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyFingerprint"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyErrorStatus"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyStorageType"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSecureShellServerHostKeyGroup = etsysSecureShellServerHostKeyGroup.setStatus('current')
etsysSecureShellServerCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 36, 2, 2, 1)).setObjects(("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerConfigGroup"), ("ENTERASYS-SECURE-SHELL-SERVER-MIB", "etsysSecureShellServerHostKeyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSecureShellServerCompliance = etsysSecureShellServerCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-SECURE-SHELL-SERVER-MIB", etsysSecureShellServerConformance=etsysSecureShellServerConformance, etsysSecureShellServerMIB=etsysSecureShellServerMIB, etsysSecureShellServerConfig=etsysSecureShellServerConfig, etsysSecureShellServerAdminMacs=etsysSecureShellServerAdminMacs, etsysSecureShellServerConfigGroup=etsysSecureShellServerConfigGroup, SshCipherList=SshCipherList, etsysSecureShellServerHostKeyType=etsysSecureShellServerHostKeyType, etsysSecureShellServerAdminPort=etsysSecureShellServerAdminPort, etsysSecureShellServerOperPort=etsysSecureShellServerOperPort, etsysSecureShellServerMac=etsysSecureShellServerMac, etsysSecureShellServerCipher=etsysSecureShellServerCipher, etsysSecureShellServerGroups=etsysSecureShellServerGroups, etsysSecureShellServerCompliances=etsysSecureShellServerCompliances, etsysSecureShellServerOperCiphers=etsysSecureShellServerOperCiphers, etsysSecureShellServerHostKeyGroup=etsysSecureShellServerHostKeyGroup, etsysSecureShellServerHostKeyOperStatus=etsysSecureShellServerHostKeyOperStatus, etsysSecureShellServerHostKeyFingerprint=etsysSecureShellServerHostKeyFingerprint, etsysSecureShellServerOperStatus=etsysSecureShellServerOperStatus, etsysSecureShellServerHostKeyRowStatus=etsysSecureShellServerHostKeyRowStatus, PYSNMP_MODULE_ID=etsysSecureShellServerMIB, etsysSecureShellServerHostKeyDate=etsysSecureShellServerHostKeyDate, etsysSecureShellServerSupportedMacs=etsysSecureShellServerSupportedMacs, SshMacList=SshMacList, etsysSecureShellServerAdminCiphers=etsysSecureShellServerAdminCiphers, etsysSecureShellServerOperMacs=etsysSecureShellServerOperMacs, etsysSecureShellServerHostKeyEntry=etsysSecureShellServerHostKeyEntry, etsysSecureShellServerHostKeySize=etsysSecureShellServerHostKeySize, etsysSecureShellServerCompliance=etsysSecureShellServerCompliance, etsysSecureShellServerErrorStatus=etsysSecureShellServerErrorStatus, etsysSecureShellServerHostKey=etsysSecureShellServerHostKey, etsysSecureShellServerHostKeyAdminStatus=etsysSecureShellServerHostKeyAdminStatus, etsysSecureShellServer=etsysSecureShellServer, etsysSecureShellServerHostKeyStorageType=etsysSecureShellServerHostKeyStorageType, etsysSecureShellServerHostKeyTable=etsysSecureShellServerHostKeyTable, etsysSecureShellServerHostKeyErrorStatus=etsysSecureShellServerHostKeyErrorStatus, etsysSecureShellServerSupportedCiphers=etsysSecureShellServerSupportedCiphers, HexString=HexString, etsysSecureShellServerAdminStatus=etsysSecureShellServerAdminStatus)
