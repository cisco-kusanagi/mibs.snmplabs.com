#
# PySNMP MIB module JUNIPER-IPSEC-FLOW-MON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-IPSEC-FLOW-MON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:48:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
jnxIpSecMibRoot, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxIpSecMibRoot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, NotificationType, Integer32, MibIdentifier, Counter32, Unsigned32, IpAddress, ObjectIdentity, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "NotificationType", "Integer32", "MibIdentifier", "Counter32", "Unsigned32", "IpAddress", "ObjectIdentity", "Bits", "TimeTicks")
TimeInterval, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "DisplayString", "TextualConvention")
jnxIpSecFlowMonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1))
jnxIpSecFlowMonMIB.setRevisions(('2007-05-16 00:00',))
if mibBuilder.loadTexts: jnxIpSecFlowMonMIB.setLastUpdated('200705112153Z')
if mibBuilder.loadTexts: jnxIpSecFlowMonMIB.setOrganization('Juniper Networks, Inc.')
jnxIpSecFlowMonNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 0))
jnxIpSecFlowMonPhaseOne = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1))
jnxIpSecFlowMonPhaseTwo = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2))
class JnxIkePeerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 0), ("idIpv4Addr", 1), ("idFqdn", 2), ("idDn", 3), ("idUfqdn", 4))

class JnxIkeNegoMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("main", 1), ("aggressive", 2))

class JnxIkeHashAlgo(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("md5", 1), ("sha", 2), ("sha256", 3))

class JnxIkeAuthMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("preSharedKey", 1), ("dssSignature", 2), ("rsaSignature", 3), ("rsaEncryption", 4), ("revRsaEncryption", 5), ("xauthPreSharedKey", 6), ("xauthDssSignature", 7), ("xauthRsaSignature", 8), ("xauthRsaEncryption", 9), ("xauthRevRsaEncryption", 10))

class JnxIkePeerRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("initiator", 1), ("responder", 2))

class JnxIkeTunStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class JnxDiffHellmanGrp(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 5))
    namedValues = NamedValues(("unknown", 0), ("modp768", 1), ("modp1024", 2), ("modp1536", 5))

class JnxKeyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("keyIke", 1), ("keyManual", 2))

class JnxEncapMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("tunnel", 1), ("transport", 2))

class JnxEncryptAlgo(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("espDes", 1), ("esp3des", 2), ("espNull", 3), ("espAes128", 4), ("espAes192", 5), ("espAes256", 6))

class JnxAuthAlgo(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("hmacMd5", 1), ("hmacSha", 2), ("hmacSha256", 3))

class JnxRemotePeerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("static", 1), ("dynamic", 2))

class JnxSpiType(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(256, 4294967295)

class JnxSAType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("manual", 1), ("dynamic", 2))

jnxIkeNumOfTunnels = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeNumOfTunnels.setStatus('current')
jnxIkeTunnelMonTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2), )
if mibBuilder.loadTexts: jnxIkeTunnelMonTable.setStatus('current')
jnxIkeTunnelMonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1), ).setIndexNames((0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTunMonRemoteGwAddrType"), (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTunMonRemoteGwAddr"), (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIkeTunMonIndex"))
if mibBuilder.loadTexts: jnxIkeTunnelMonEntry.setStatus('current')
jnxIkeTunMonRemoteGwAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: jnxIkeTunMonRemoteGwAddrType.setStatus('current')
jnxIkeTunMonRemoteGwAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 2), InetAddress())
if mibBuilder.loadTexts: jnxIkeTunMonRemoteGwAddr.setStatus('current')
jnxIkeTunMonIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: jnxIkeTunMonIndex.setStatus('current')
jnxIkeTunMonLocalGwAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 4), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonLocalGwAddr.setStatus('current')
jnxIkeTunMonLocalGwAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 5), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonLocalGwAddrType.setStatus('current')
jnxIkeTunMonState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 6), JnxIkeTunStateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonState.setStatus('current')
jnxIkeTunMonInitiatorCookie = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonInitiatorCookie.setStatus('current')
jnxIkeTunMonResponderCookie = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonResponderCookie.setStatus('current')
jnxIkeTunMonLocalRole = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 9), JnxIkePeerRole()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonLocalRole.setStatus('current')
jnxIkeTunMonLocalIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 10), JnxIkePeerType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonLocalIdType.setStatus('current')
jnxIkeTunMonLocalIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonLocalIdValue.setStatus('current')
jnxIkeTunMonLocalCertName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonLocalCertName.setStatus('current')
jnxIkeTunMonRemoteIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 13), JnxIkePeerType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonRemoteIdType.setStatus('current')
jnxIkeTunMonRemoteIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonRemoteIdValue.setStatus('current')
jnxIkeTunMonNegoMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 15), JnxIkeNegoMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonNegoMode.setStatus('current')
jnxIkeTunMonDiffHellmanGrp = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 16), JnxDiffHellmanGrp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonDiffHellmanGrp.setStatus('current')
jnxIkeTunMonEncryptAlgo = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 17), JnxEncryptAlgo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonEncryptAlgo.setStatus('current')
jnxIkeTunMonHashAlgo = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 18), JnxIkeHashAlgo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonHashAlgo.setStatus('current')
jnxIkeTunMonAuthMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 19), JnxIkeAuthMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonAuthMethod.setStatus('current')
jnxIkeTunMonLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonLifeTime.setStatus('current')
jnxIkeTunMonActiveTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 21), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonActiveTime.setStatus('current')
jnxIkeTunMonInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 22), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonInOctets.setStatus('current')
jnxIkeTunMonInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 23), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonInPkts.setStatus('current')
jnxIkeTunMonOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 24), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonOutOctets.setStatus('current')
jnxIkeTunMonOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 25), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonOutPkts.setStatus('current')
jnxIkeTunMonXAuthUserId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 26), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonXAuthUserId.setStatus('current')
jnxIkeTunMonDPDDownCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 1, 2, 1, 27), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIkeTunMonDPDDownCount.setStatus('obsolete')
jnxIpSecNumOfTunnels = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecNumOfTunnels.setStatus('current')
jnxIpSecTunnelMonTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2), )
if mibBuilder.loadTexts: jnxIpSecTunnelMonTable.setStatus('current')
jnxIpSecTunnelMonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1), ).setIndexNames((0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunMonRemoteGwAddrType"), (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunMonRemoteGwAddr"), (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunMonIndex"))
if mibBuilder.loadTexts: jnxIpSecTunnelMonEntry.setStatus('current')
jnxIpSecTunMonRemoteGwAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 1), InetAddressType())
if mibBuilder.loadTexts: jnxIpSecTunMonRemoteGwAddrType.setStatus('current')
jnxIpSecTunMonRemoteGwAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 2), InetAddress())
if mibBuilder.loadTexts: jnxIpSecTunMonRemoteGwAddr.setStatus('current')
jnxIpSecTunMonIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: jnxIpSecTunMonIndex.setStatus('current')
jnxIpSecTunMonLocalGwAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonLocalGwAddrType.setStatus('current')
jnxIpSecTunMonLocalGwAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonLocalGwAddr.setStatus('current')
jnxIpSecTunMonLocalProxyId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonLocalProxyId.setStatus('current')
jnxIpSecTunMonRemoteProxyId = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonRemoteProxyId.setStatus('current')
jnxIpSecTunMonKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 8), JnxKeyType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonKeyType.setStatus('current')
jnxIpSecTunMonRemotePeerType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 9), JnxRemotePeerType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonRemotePeerType.setStatus('current')
jnxIpSecTunMonOutEncryptedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonOutEncryptedBytes.setStatus('current')
jnxIpSecTunMonOutEncryptedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonOutEncryptedPkts.setStatus('current')
jnxIpSecTunMonInDecryptedBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonInDecryptedBytes.setStatus('current')
jnxIpSecTunMonInDecryptedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonInDecryptedPkts.setStatus('current')
jnxIpSecTunMonAHInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonAHInBytes.setStatus('current')
jnxIpSecTunMonAHInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonAHInPkts.setStatus('current')
jnxIpSecTunMonAHOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonAHOutBytes.setStatus('current')
jnxIpSecTunMonAHOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonAHOutPkts.setStatus('current')
jnxIpSecTunMonReplayDropPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonReplayDropPkts.setStatus('current')
jnxIpSecTunMonAhAuthFails = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonAhAuthFails.setStatus('current')
jnxIpSecTunMonEspAuthFails = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonEspAuthFails.setStatus('current')
jnxIpSecTunMonDecryptFails = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonDecryptFails.setStatus('current')
jnxIpSecTunMonBadHeaders = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonBadHeaders.setStatus('current')
jnxIpSecTunMonBadTrailers = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonBadTrailers.setStatus('current')
jnxIpSecTunMonDroppedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 2, 1, 26), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecTunMonDroppedPkts.setStatus('obsolete')
jnxIpSecSaMonTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3), )
if mibBuilder.loadTexts: jnxIpSecSaMonTable.setStatus('current')
jnxIpSecSaMonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1), ).setIndexNames((0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunMonRemoteGwAddrType"), (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunMonRemoteGwAddr"), (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunMonIndex"), (0, "JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecSaMonIndex"))
if mibBuilder.loadTexts: jnxIpSecSaMonEntry.setStatus('current')
jnxIpSecSaMonIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: jnxIpSecSaMonIndex.setStatus('current')
jnxIpSecSaMonProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ah", 1), ("esp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecSaMonProtocol.setStatus('current')
jnxIpSecSaMonInSpi = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 3), JnxSpiType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecSaMonInSpi.setStatus('current')
jnxIpSecSaMonOutSpi = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 4), JnxSpiType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecSaMonOutSpi.setStatus('current')
jnxIpSecSaMonType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 5), JnxSAType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecSaMonType.setStatus('current')
jnxIpSecSaMonEncapMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 6), JnxEncapMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecSaMonEncapMode.setStatus('current')
jnxIpSecSaMonLifeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecSaMonLifeSize.setStatus('current')
jnxIpSecSaMonLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecSaMonLifeTime.setStatus('current')
jnxIpSecSaMonActiveTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 9), TimeInterval()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecSaMonActiveTime.setStatus('current')
jnxIpSecSaMonLifeSizeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecSaMonLifeSizeThreshold.setStatus('current')
jnxIpSecSaMonLifeTimeThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecSaMonLifeTimeThreshold.setStatus('current')
jnxIpSecSaMonEncryptAlgo = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 12), JnxEncryptAlgo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecSaMonEncryptAlgo.setStatus('current')
jnxIpSecSaMonAuthAlgo = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 13), JnxAuthAlgo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecSaMonAuthAlgo.setStatus('current')
jnxIpSecSaMonState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 52, 1, 2, 3, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("active", 1), ("expiring", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxIpSecSaMonState.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-IPSEC-FLOW-MON-MIB", JnxDiffHellmanGrp=JnxDiffHellmanGrp, jnxIpSecTunMonAHInBytes=jnxIpSecTunMonAHInBytes, jnxIpSecTunMonReplayDropPkts=jnxIpSecTunMonReplayDropPkts, JnxEncryptAlgo=JnxEncryptAlgo, jnxIpSecTunMonRemoteProxyId=jnxIpSecTunMonRemoteProxyId, jnxIkeTunMonRemoteGwAddr=jnxIkeTunMonRemoteGwAddr, jnxIpSecTunMonOutEncryptedPkts=jnxIpSecTunMonOutEncryptedPkts, JnxIkeAuthMethod=JnxIkeAuthMethod, jnxIpSecTunMonInDecryptedPkts=jnxIpSecTunMonInDecryptedPkts, JnxIkePeerType=JnxIkePeerType, jnxIpSecTunMonRemoteGwAddr=jnxIpSecTunMonRemoteGwAddr, jnxIpSecSaMonEncryptAlgo=jnxIpSecSaMonEncryptAlgo, jnxIpSecTunMonAhAuthFails=jnxIpSecTunMonAhAuthFails, jnxIpSecSaMonIndex=jnxIpSecSaMonIndex, jnxIpSecTunMonAHOutPkts=jnxIpSecTunMonAHOutPkts, jnxIkeTunMonLocalIdValue=jnxIkeTunMonLocalIdValue, jnxIkeTunMonRemoteIdType=jnxIkeTunMonRemoteIdType, jnxIpSecTunMonRemoteGwAddrType=jnxIpSecTunMonRemoteGwAddrType, jnxIkeTunMonLocalGwAddrType=jnxIkeTunMonLocalGwAddrType, jnxIkeTunMonDPDDownCount=jnxIkeTunMonDPDDownCount, jnxIpSecTunMonIndex=jnxIpSecTunMonIndex, jnxIpSecTunMonBadTrailers=jnxIpSecTunMonBadTrailers, jnxIpSecTunMonLocalGwAddr=jnxIpSecTunMonLocalGwAddr, jnxIkeTunMonLocalRole=jnxIkeTunMonLocalRole, jnxIkeNumOfTunnels=jnxIkeNumOfTunnels, jnxIkeTunMonInitiatorCookie=jnxIkeTunMonInitiatorCookie, jnxIpSecSaMonLifeTime=jnxIpSecSaMonLifeTime, jnxIkeTunMonRemoteGwAddrType=jnxIkeTunMonRemoteGwAddrType, JnxRemotePeerType=JnxRemotePeerType, jnxIkeTunMonEncryptAlgo=jnxIkeTunMonEncryptAlgo, jnxIpSecTunMonEspAuthFails=jnxIpSecTunMonEspAuthFails, jnxIpSecTunnelMonEntry=jnxIpSecTunnelMonEntry, jnxIpSecTunMonLocalProxyId=jnxIpSecTunMonLocalProxyId, JnxIkeTunStateType=JnxIkeTunStateType, JnxAuthAlgo=JnxAuthAlgo, jnxIpSecTunMonInDecryptedBytes=jnxIpSecTunMonInDecryptedBytes, PYSNMP_MODULE_ID=jnxIpSecFlowMonMIB, jnxIpSecSaMonInSpi=jnxIpSecSaMonInSpi, jnxIkeTunMonLocalGwAddr=jnxIkeTunMonLocalGwAddr, jnxIpSecTunMonLocalGwAddrType=jnxIpSecTunMonLocalGwAddrType, jnxIpSecTunMonAHInPkts=jnxIpSecTunMonAHInPkts, jnxIpSecFlowMonPhaseOne=jnxIpSecFlowMonPhaseOne, jnxIkeTunMonAuthMethod=jnxIkeTunMonAuthMethod, jnxIkeTunMonLocalIdType=jnxIkeTunMonLocalIdType, JnxSAType=JnxSAType, jnxIpSecTunMonBadHeaders=jnxIpSecTunMonBadHeaders, jnxIkeTunMonXAuthUserId=jnxIkeTunMonXAuthUserId, jnxIpSecSaMonActiveTime=jnxIpSecSaMonActiveTime, jnxIpSecSaMonLifeTimeThreshold=jnxIpSecSaMonLifeTimeThreshold, jnxIkeTunMonLifeTime=jnxIkeTunMonLifeTime, jnxIpSecTunMonOutEncryptedBytes=jnxIpSecTunMonOutEncryptedBytes, jnxIkeTunnelMonEntry=jnxIkeTunnelMonEntry, jnxIpSecNumOfTunnels=jnxIpSecNumOfTunnels, JnxEncapMode=JnxEncapMode, JnxSpiType=JnxSpiType, JnxKeyType=JnxKeyType, jnxIkeTunnelMonTable=jnxIkeTunnelMonTable, jnxIkeTunMonOutPkts=jnxIkeTunMonOutPkts, jnxIkeTunMonInPkts=jnxIkeTunMonInPkts, jnxIkeTunMonIndex=jnxIkeTunMonIndex, jnxIpSecTunMonDroppedPkts=jnxIpSecTunMonDroppedPkts, jnxIpSecTunMonKeyType=jnxIpSecTunMonKeyType, jnxIkeTunMonHashAlgo=jnxIkeTunMonHashAlgo, jnxIpSecSaMonTable=jnxIpSecSaMonTable, jnxIkeTunMonActiveTime=jnxIkeTunMonActiveTime, jnxIpSecSaMonAuthAlgo=jnxIpSecSaMonAuthAlgo, jnxIkeTunMonResponderCookie=jnxIkeTunMonResponderCookie, jnxIpSecSaMonLifeSizeThreshold=jnxIpSecSaMonLifeSizeThreshold, JnxIkeHashAlgo=JnxIkeHashAlgo, jnxIpSecSaMonEntry=jnxIpSecSaMonEntry, jnxIpSecTunMonAHOutBytes=jnxIpSecTunMonAHOutBytes, JnxIkePeerRole=JnxIkePeerRole, jnxIpSecTunnelMonTable=jnxIpSecTunnelMonTable, JnxIkeNegoMode=JnxIkeNegoMode, jnxIpSecFlowMonNotifications=jnxIpSecFlowMonNotifications, jnxIkeTunMonState=jnxIkeTunMonState, jnxIpSecSaMonEncapMode=jnxIpSecSaMonEncapMode, jnxIpSecSaMonProtocol=jnxIpSecSaMonProtocol, jnxIkeTunMonNegoMode=jnxIkeTunMonNegoMode, jnxIkeTunMonLocalCertName=jnxIkeTunMonLocalCertName, jnxIkeTunMonDiffHellmanGrp=jnxIkeTunMonDiffHellmanGrp, jnxIpSecSaMonState=jnxIpSecSaMonState, jnxIpSecSaMonOutSpi=jnxIpSecSaMonOutSpi, jnxIkeTunMonOutOctets=jnxIkeTunMonOutOctets, jnxIkeTunMonInOctets=jnxIkeTunMonInOctets, jnxIpSecSaMonType=jnxIpSecSaMonType, jnxIpSecTunMonRemotePeerType=jnxIpSecTunMonRemotePeerType, jnxIpSecFlowMonPhaseTwo=jnxIpSecFlowMonPhaseTwo, jnxIkeTunMonRemoteIdValue=jnxIkeTunMonRemoteIdValue, jnxIpSecSaMonLifeSize=jnxIpSecSaMonLifeSize, jnxIpSecFlowMonMIB=jnxIpSecFlowMonMIB, jnxIpSecTunMonDecryptFails=jnxIpSecTunMonDecryptFails)
