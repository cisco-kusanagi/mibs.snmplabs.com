#
# PySNMP MIB module ONEACCESS-GDOI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-GDOI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:25:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
oacExpIMManagement, = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMManagement")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, MibIdentifier, Integer32, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, ObjectIdentity, Counter32, Counter64, Unsigned32, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "Integer32", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "ObjectIdentity", "Counter32", "Counter64", "Unsigned32", "NotificationType", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
oacExpIMGdoiMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224))
if mibBuilder.loadTexts: oacExpIMGdoiMIB.setLastUpdated('1404151200Z')
if mibBuilder.loadTexts: oacExpIMGdoiMIB.setOrganization('ONE ACCESS')
class OacGdoiIdentificationType(TextualConvention, Integer32):
    reference = "IANA ISAKMP Registry - 'Magic Numbers' for ISAKMP Protocol Section: IPSEC Identification Type http://www.iana.org/assignments/isakmp-registry"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("keyID", 1), ("ipv4", 2))

class OacGdoiIdentificationValue(TextualConvention, OctetString):
    reference = "IANA ISAKMP Registry - 'Magic Numbers' for ISAKMP Protocol Section: IPSEC Identification Type http://www.iana.org/assignments/isakmp-registry"
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class OacGdoiSPI(TextualConvention, OctetString):
    reference = 'RFC 3547 - Section: 5.3. SA KEK Payload'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(32, 32)
    fixedLength = 32

class OacGdoiKEKEncryptionAlgorithm(TextualConvention, Integer32):
    reference = "IANA IKEv2 Parameters Section: Encryption Algorithm Transform IDs http://www.iana.org/assignments/ikev2-parameters IANA 'Magic Numbers' for ISAMP Protocol Section: IPSEC ESP Transform Identifiers http://www.iana.org/assignments/isakmp-registry RFC 2407 - Section: 4.4.4. IPSEC ESP Transform Identifiers RFC 3547 - Section: 5.3.3. KEK_ALGORITHM RFC 4306 - Section: 3.3.2. Transform Substructure RFC 4106, 4309, 4543, 5282, 5529"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enc-des", 1), ("enc-3des", 2), ("enc-aes", 3))

class OacGdoiHashAlogrithm(TextualConvention, Integer32):
    reference = 'IANA IKEv2 Parameters Section: Pseudo-random Function Transform IDs http://www.iana.org/assignments/ikev2-parameters RFC 3547 - Section: 5.3.6. SIG_HASH_ALGORITHM RFC 4306 - Section: 3.3.2. Transform Substructure RFC 4615, 4868'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("md5", 1), ("sha1", 2))

class OacGdoiSignatureMethod(TextualConvention, Integer32):
    reference = 'IANA IKEv2 Parameters Section: Integrity Algorithm Transform IDs http://www.iana.org/assignments/ikev2-parameters RFC 2407 - Section: 4.5. IPSEC Security Assoc. Attributes RFC 3547 - Section: 5.3.6. SIG_HASH_ALGORITHM RFC 4306 - Section: 3.3.2. Transform Substructure RFC 4494, 4543, 4595, 4868'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rsa", 1), ("dss", 2), ("ecdss", 3))

oacGdoiMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1))
oacGdoiGroupTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 1), )
if mibBuilder.loadTexts: oacGdoiGroupTable.setStatus('current')
oacGdoiGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 1, 1), ).setIndexNames((0, "ONEACCESS-GDOI-MIB", "oacGdoiGroupName"))
if mibBuilder.loadTexts: oacGdoiGroupEntry.setStatus('current')
oacGdoiGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGroupName.setStatus('current')
oacGdoiGroupIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 1, 1, 2), OacGdoiIdentificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGroupIdType.setStatus('current')
oacGdoiGroupIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 1, 1, 3), OacGdoiIdentificationValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGroupIdValue.setStatus('current')
oacGdoiGm = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2))
oacGdoiPolicy = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3))
oacGdoiGmTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2), )
if mibBuilder.loadTexts: oacGdoiGmTable.setStatus('current')
oacGdoiGmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1), ).setIndexNames((0, "ONEACCESS-GDOI-MIB", "oacGdoiGroupName"), (0, "ONEACCESS-GDOI-MIB", "oacGdoiGmActiveKEK"))
if mibBuilder.loadTexts: oacGdoiGmEntry.setStatus('current')
oacGdoiGmIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1, 1), OacGdoiIdentificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmIdType.setStatus('current')
oacGdoiGmIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1, 2), OacGdoiIdentificationValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmIdValue.setStatus('current')
oacGdoiGmRegKeyServerIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1, 3), OacGdoiIdentificationValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmRegKeyServerIdValue.setStatus('current')
oacGdoiGmActiveKEK = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1, 4), OacGdoiSPI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmActiveKEK.setStatus('current')
oacGdoiGmRekeysReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1, 5), Counter32()).setUnits('GROUPKEY-PUSH Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmRekeysReceived.setStatus('current')
oacGdoiGmKekTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2), )
if mibBuilder.loadTexts: oacGdoiGmKekTable.setStatus('current')
oacGdoiGmKekEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1), ).setIndexNames((0, "ONEACCESS-GDOI-MIB", "oacGdoiGroupName"), (0, "ONEACCESS-GDOI-MIB", "oacGdoiGmKekSPI"))
if mibBuilder.loadTexts: oacGdoiGmKekEntry.setStatus('current')
oacGdoiGmKekSPI = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 1), OacGdoiSPI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekSPI.setStatus('current')
oacGdoiGmKekSrcIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 2), OacGdoiIdentificationValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekSrcIdValue.setStatus('current')
oacGdoiGmKekDstIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 3), OacGdoiIdentificationValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekDstIdValue.setStatus('current')
oacGdoiGmKekEncryptAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 4), OacGdoiKEKEncryptionAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekEncryptAlg.setStatus('current')
oacGdoiGmKekEncryptKeyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 5), Unsigned32()).setUnits('Bits').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekEncryptKeyLength.setStatus('current')
oacGdoiGmKekSigHashAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 6), OacGdoiHashAlogrithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekSigHashAlg.setStatus('current')
oacGdoiGmKekSigAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 7), OacGdoiSignatureMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekSigAlg.setStatus('current')
oacGdoiGmKekSigKeyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 8), Unsigned32()).setUnits('Bits').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekSigKeyLength.setStatus('current')
oacGdoiGmKekOriginalLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 9), Unsigned32()).setUnits('Seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekOriginalLifetime.setStatus('current')
oacGdoiGmKekRemainingLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 10), Unsigned32()).setUnits('Seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekRemainingLifetime.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-GDOI-MIB", oacGdoiGm=oacGdoiGm, oacGdoiMIBObjects=oacGdoiMIBObjects, oacGdoiGmKekSPI=oacGdoiGmKekSPI, oacGdoiGroupIdType=oacGdoiGroupIdType, oacGdoiGmKekSigHashAlg=oacGdoiGmKekSigHashAlg, OacGdoiIdentificationValue=OacGdoiIdentificationValue, oacGdoiGmKekSigAlg=oacGdoiGmKekSigAlg, oacGdoiGmEntry=oacGdoiGmEntry, oacGdoiGmKekRemainingLifetime=oacGdoiGmKekRemainingLifetime, oacGdoiPolicy=oacGdoiPolicy, oacGdoiGmIdType=oacGdoiGmIdType, oacExpIMGdoiMIB=oacExpIMGdoiMIB, oacGdoiGroupEntry=oacGdoiGroupEntry, OacGdoiSPI=OacGdoiSPI, OacGdoiIdentificationType=OacGdoiIdentificationType, oacGdoiGmKekSigKeyLength=oacGdoiGmKekSigKeyLength, oacGdoiGmActiveKEK=oacGdoiGmActiveKEK, oacGdoiGmKekDstIdValue=oacGdoiGmKekDstIdValue, oacGdoiGmIdValue=oacGdoiGmIdValue, oacGdoiGroupIdValue=oacGdoiGroupIdValue, oacGdoiGmKekSrcIdValue=oacGdoiGmKekSrcIdValue, oacGdoiGmRekeysReceived=oacGdoiGmRekeysReceived, oacGdoiGmRegKeyServerIdValue=oacGdoiGmRegKeyServerIdValue, PYSNMP_MODULE_ID=oacExpIMGdoiMIB, oacGdoiGmKekEncryptAlg=oacGdoiGmKekEncryptAlg, oacGdoiGroupTable=oacGdoiGroupTable, oacGdoiGmKekEncryptKeyLength=oacGdoiGmKekEncryptKeyLength, OacGdoiKEKEncryptionAlgorithm=OacGdoiKEKEncryptionAlgorithm, OacGdoiSignatureMethod=OacGdoiSignatureMethod, oacGdoiGroupName=oacGdoiGroupName, oacGdoiGmTable=oacGdoiGmTable, oacGdoiGmKekOriginalLifetime=oacGdoiGmKekOriginalLifetime, oacGdoiGmKekTable=oacGdoiGmKekTable, OacGdoiHashAlogrithm=OacGdoiHashAlogrithm, oacGdoiGmKekEntry=oacGdoiGmKekEntry)
