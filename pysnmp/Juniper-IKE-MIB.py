#
# PySNMP MIB module Juniper-IKE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-IKE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:52:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, Counter32, Bits, Integer32, ModuleIdentity, NotificationType, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Counter64, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "Bits", "Integer32", "ModuleIdentity", "NotificationType", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Counter64", "Unsigned32", "TimeTicks")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
juniIkeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71))
juniIkeMIB.setRevisions(('2005-11-22 16:15', '2004-01-23 15:12', '2004-04-06 22:26',))
if mibBuilder.loadTexts: juniIkeMIB.setLastUpdated('200404062226Z')
if mibBuilder.loadTexts: juniIkeMIB.setOrganization('Juniper Networks, Inc.')
class JuniIkeAuthenticationMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 3))
    namedValues = NamedValues(("rsaSignature", 0), ("preSharedKeys", 3))

class JuniIkeEncryptionMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("des", 0), ("tripleDes", 1))

class JuniIkeGroup(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 4))
    namedValues = NamedValues(("group1", 0), ("group2", 1), ("group5", 4))

class JuniIkeHashMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("md5", 0), ("sha", 1))

class JuniIkeNegotiationMode(TextualConvention, Integer32):
    status = 'obsolete'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("aggressive", 0), ("main", 1))

class JuniIkeNegotiationV2Mode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("aggressiveAccepted", 0), ("aggressiveRequested", 1), ("aggressiveRequired", 2), ("aggressiveNotAllowed", 3))

class JuniIpsecPhase1SaState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26))
    namedValues = NamedValues(("reserved", 0), ("startSaNegotiationI", 1), ("startSaNegotiationR", 2), ("mmSaI", 3), ("mmSaR", 4), ("mmKeI", 5), ("mmKeR", 6), ("mmFinalI", 7), ("mmFinalR", 8), ("mmDoneI", 9), ("amSaI", 10), ("amSaR", 11), ("amFinalI", 12), ("amDoneR", 13), ("startQmI", 14), ("startQmR", 15), ("qmHashSaI", 16), ("qmHashSaR", 17), ("qmHashI", 18), ("qmDoneR", 19), ("startNgmI", 20), ("startNgmR", 21), ("ngmHashSaI", 22), ("ngmHashSaR", 23), ("ngmDoneI", 24), ("done", 25), ("deleted", 26))

class JuniIpsecPhase1SaDirection(TextualConvention, Integer32):
    status = 'obsolete'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("initiator", 0), ("responder", 1))

juniIkeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1))
juniIke = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1))
juniIkePolicyRuleTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 1), )
if mibBuilder.loadTexts: juniIkePolicyRuleTable.setStatus('obsolete')
juniIkePolicyRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 1, 1), ).setIndexNames((0, "Juniper-IKE-MIB", "juniIkePolicyRulePriority"))
if mibBuilder.loadTexts: juniIkePolicyRuleEntry.setStatus('obsolete')
juniIkePolicyRulePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000)))
if mibBuilder.loadTexts: juniIkePolicyRulePriority.setStatus('obsolete')
juniIkePolicyRuleAuthMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 1, 1, 2), JuniIkeAuthenticationMethod().clone('preSharedKeys')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkePolicyRuleAuthMethod.setStatus('obsolete')
juniIkePolicyRuleEncryptMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 1, 1, 3), JuniIkeEncryptionMethod().clone('tripleDes')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkePolicyRuleEncryptMethod.setStatus('obsolete')
juniIkePolicyRulePfsGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 1, 1, 4), JuniIkeGroup().clone('group2')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkePolicyRulePfsGroup.setStatus('obsolete')
juniIkePolicyRuleHashMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 1, 1, 5), JuniIkeHashMethod().clone('sha')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkePolicyRuleHashMethod.setStatus('obsolete')
juniIkePolicyRuleLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 86400)).clone(28800)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkePolicyRuleLifetime.setStatus('obsolete')
juniIkePolicyRuleNegotiationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 1, 1, 7), JuniIkeNegotiationMode().clone('aggressive')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkePolicyRuleNegotiationMode.setStatus('obsolete')
juniIkePolicyRuleRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkePolicyRuleRowStatus.setStatus('obsolete')
juniIkePolicyRuleV2Table = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6), )
if mibBuilder.loadTexts: juniIkePolicyRuleV2Table.setStatus('current')
juniIkePolicyRuleV2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1), ).setIndexNames((0, "Juniper-IKE-MIB", "juniIkePolicyRuleV2Priority"))
if mibBuilder.loadTexts: juniIkePolicyRuleV2Entry.setStatus('current')
juniIkePolicyRuleV2Priority = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000)))
if mibBuilder.loadTexts: juniIkePolicyRuleV2Priority.setStatus('current')
juniIkePolicyRuleV2AuthMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1, 2), JuniIkeAuthenticationMethod().clone('preSharedKeys')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkePolicyRuleV2AuthMethod.setStatus('current')
juniIkePolicyRuleV2EncryptMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1, 3), JuniIkeEncryptionMethod().clone('tripleDes')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkePolicyRuleV2EncryptMethod.setStatus('current')
juniIkePolicyRuleV2PfsGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1, 4), JuniIkeGroup().clone('group2')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkePolicyRuleV2PfsGroup.setStatus('current')
juniIkePolicyRuleV2HashMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1, 5), JuniIkeHashMethod().clone('sha')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkePolicyRuleV2HashMethod.setStatus('current')
juniIkePolicyRuleV2Lifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 86400)).clone(28800)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkePolicyRuleV2Lifetime.setStatus('current')
juniIkePolicyRuleV2NegotiationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1, 7), JuniIkeNegotiationV2Mode().clone('aggressiveNotAllowed')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkePolicyRuleV2NegotiationMode.setStatus('current')
juniIkePolicyRuleV2IpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1, 8), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkePolicyRuleV2IpAddress.setStatus('current')
juniIkePolicyRuleV2RouterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1, 9), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkePolicyRuleV2RouterIndex.setStatus('current')
juniIkePolicyRuleV2RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 6, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkePolicyRuleV2RowStatus.setStatus('current')
juniIkeIpv4PresharedKeyTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 2), )
if mibBuilder.loadTexts: juniIkeIpv4PresharedKeyTable.setStatus('current')
juniIkeIpv4PresharedKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 2, 1), ).setIndexNames((0, "Juniper-IKE-MIB", "juniIkeIpv4PresharedRemoteIpAddr"), (0, "Juniper-IKE-MIB", "juniIkeIpv4PresharedRouterIdx"))
if mibBuilder.loadTexts: juniIkeIpv4PresharedKeyEntry.setStatus('current')
juniIkeIpv4PresharedRemoteIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: juniIkeIpv4PresharedRemoteIpAddr.setStatus('current')
juniIkeIpv4PresharedRouterIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 2, 1, 2), Unsigned32())
if mibBuilder.loadTexts: juniIkeIpv4PresharedRouterIdx.setStatus('current')
juniIkeIpv4PresharedKeyStr = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 200))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkeIpv4PresharedKeyStr.setStatus('current')
juniIkeIpv4PresharedMaskedKeyStr = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 2, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 300))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkeIpv4PresharedMaskedKeyStr.setStatus('current')
juniIkeIpv4PresharedKeyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkeIpv4PresharedKeyRowStatus.setStatus('current')
juniIkeFqdnPresharedKeyTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 3), )
if mibBuilder.loadTexts: juniIkeFqdnPresharedKeyTable.setStatus('current')
juniIkeFqdnPresharedKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 3, 1), ).setIndexNames((0, "Juniper-IKE-MIB", "juniIkeFqdnPresharedRemote"), (0, "Juniper-IKE-MIB", "juniIkeFqdnPresharedRouterIndex"))
if mibBuilder.loadTexts: juniIkeFqdnPresharedKeyEntry.setStatus('current')
juniIkeFqdnPresharedRemote = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80)))
if mibBuilder.loadTexts: juniIkeFqdnPresharedRemote.setStatus('current')
juniIkeFqdnPresharedRouterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: juniIkeFqdnPresharedRouterIndex.setStatus('current')
juniIkeFqdnPresharedKeyStr = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 200))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkeFqdnPresharedKeyStr.setStatus('current')
juniIkeFqdnPresharedMaskedKeyStr = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 3, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 300))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkeFqdnPresharedMaskedKeyStr.setStatus('current')
juniIkeFqdnPresharedKeyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniIkeFqdnPresharedKeyRowStatus.setStatus('current')
juniIkeSaTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 4), )
if mibBuilder.loadTexts: juniIkeSaTable.setStatus('obsolete')
juniIkeSaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 4, 1), ).setIndexNames((0, "Juniper-IKE-MIB", "juniIkeSaRemoteIpAddr"), (0, "Juniper-IKE-MIB", "juniIkeSaLocalIpAddr"), (0, "Juniper-IKE-MIB", "juniIkeSaRouterIndex"), (0, "Juniper-IKE-MIB", "juniIkeSaDirection"))
if mibBuilder.loadTexts: juniIkeSaEntry.setStatus('obsolete')
juniIkeSaRemoteIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: juniIkeSaRemoteIpAddr.setStatus('obsolete')
juniIkeSaLocalIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 4, 1, 2), IpAddress())
if mibBuilder.loadTexts: juniIkeSaLocalIpAddr.setStatus('obsolete')
juniIkeSaRouterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 4, 1, 3), Unsigned32())
if mibBuilder.loadTexts: juniIkeSaRouterIndex.setStatus('obsolete')
juniIkeSaDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 4, 1, 4), JuniIpsecPhase1SaDirection())
if mibBuilder.loadTexts: juniIkeSaDirection.setStatus('obsolete')
juniIkeSaState = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 4, 1, 5), JuniIpsecPhase1SaState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIkeSaState.setStatus('obsolete')
juniIkeSaRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 4, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIkeSaRemaining.setStatus('obsolete')
juniIkeSa2Table = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5), )
if mibBuilder.loadTexts: juniIkeSa2Table.setStatus('current')
juniIkeSa2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1), ).setIndexNames((0, "Juniper-IKE-MIB", "juniIkeSa2RemoteIpAddr"), (0, "Juniper-IKE-MIB", "juniIkeSaRemotePort"), (0, "Juniper-IKE-MIB", "juniIkeSa2LocalIpAddr"), (0, "Juniper-IKE-MIB", "juniIkeSaLocalPort"), (0, "Juniper-IKE-MIB", "juniIkeSa2RouterIndex"), (0, "Juniper-IKE-MIB", "juniIkeSa2Direction"), (0, "Juniper-IKE-MIB", "juniIkeSaNegotiationDone"))
if mibBuilder.loadTexts: juniIkeSa2Entry.setStatus('current')
juniIkeSa2RemoteIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: juniIkeSa2RemoteIpAddr.setStatus('current')
juniIkeSaRemotePort = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 2), Unsigned32())
if mibBuilder.loadTexts: juniIkeSaRemotePort.setStatus('current')
juniIkeSa2LocalIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 3), IpAddress())
if mibBuilder.loadTexts: juniIkeSa2LocalIpAddr.setStatus('current')
juniIkeSaLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 4), Unsigned32())
if mibBuilder.loadTexts: juniIkeSaLocalPort.setStatus('current')
juniIkeSa2RouterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 5), Unsigned32())
if mibBuilder.loadTexts: juniIkeSa2RouterIndex.setStatus('current')
juniIkeSa2Direction = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("responder", 0), ("initiator", 1))))
if mibBuilder.loadTexts: juniIkeSa2Direction.setStatus('current')
juniIkeSaNegotiationDone = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("negotiationNotDone", 0), ("negotiationDone", 1))))
if mibBuilder.loadTexts: juniIkeSaNegotiationDone.setStatus('current')
juniIkeSa2State = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 8), JuniIpsecPhase1SaState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIkeSa2State.setStatus('current')
juniIkeSa2Remaining = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 86400))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: juniIkeSa2Remaining.setStatus('current')
juniRemoteCookie = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniRemoteCookie.setStatus('current')
juniLocalCookie = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 1, 1, 5, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniLocalCookie.setStatus('current')
juniIkeMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2))
juniIkeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 1))
juniIkeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 2))
juniIkeCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 1, 1)).setObjects(("Juniper-IKE-MIB", "juniIkePolicyRuleGroup"), ("Juniper-IKE-MIB", "juniIkeIpv4PreSharedKeyGroup"), ("Juniper-IKE-MIB", "juniIkeFqdnPreSharedKeyGroup"), ("Juniper-IKE-MIB", "juniIkeSaGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIkeCompliance = juniIkeCompliance.setStatus('obsolete')
juniIkeCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 1, 2)).setObjects(("Juniper-IKE-MIB", "juniIkePolicyRuleGroup"), ("Juniper-IKE-MIB", "juniIkeIpv4PreSharedKeyGroup"), ("Juniper-IKE-MIB", "juniIkeFqdnPreSharedKeyGroup"), ("Juniper-IKE-MIB", "juniIkeSa2Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIkeCompliance2 = juniIkeCompliance2.setStatus('obsolete')
juniIkeCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 1, 3)).setObjects(("Juniper-IKE-MIB", "juniIkePolicyRuleV2Group"), ("Juniper-IKE-MIB", "juniIkeIpv4PreSharedKeyGroup"), ("Juniper-IKE-MIB", "juniIkeFqdnPreSharedKeyGroup"), ("Juniper-IKE-MIB", "juniIkeSa2Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIkeCompliance3 = juniIkeCompliance3.setStatus('current')
juniIkePolicyRuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 2, 1)).setObjects(("Juniper-IKE-MIB", "juniIkePolicyRuleAuthMethod"), ("Juniper-IKE-MIB", "juniIkePolicyRuleEncryptMethod"), ("Juniper-IKE-MIB", "juniIkePolicyRulePfsGroup"), ("Juniper-IKE-MIB", "juniIkePolicyRuleHashMethod"), ("Juniper-IKE-MIB", "juniIkePolicyRuleLifetime"), ("Juniper-IKE-MIB", "juniIkePolicyRuleNegotiationMode"), ("Juniper-IKE-MIB", "juniIkePolicyRuleRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIkePolicyRuleGroup = juniIkePolicyRuleGroup.setStatus('obsolete')
juniIkeIpv4PreSharedKeyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 2, 2)).setObjects(("Juniper-IKE-MIB", "juniIkeIpv4PresharedKeyStr"), ("Juniper-IKE-MIB", "juniIkeIpv4PresharedMaskedKeyStr"), ("Juniper-IKE-MIB", "juniIkeIpv4PresharedKeyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIkeIpv4PreSharedKeyGroup = juniIkeIpv4PreSharedKeyGroup.setStatus('current')
juniIkeFqdnPreSharedKeyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 2, 3)).setObjects(("Juniper-IKE-MIB", "juniIkeFqdnPresharedKeyStr"), ("Juniper-IKE-MIB", "juniIkeFqdnPresharedMaskedKeyStr"), ("Juniper-IKE-MIB", "juniIkeFqdnPresharedKeyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIkeFqdnPreSharedKeyGroup = juniIkeFqdnPreSharedKeyGroup.setStatus('current')
juniIkeSaGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 2, 4)).setObjects(("Juniper-IKE-MIB", "juniIkeSaState"), ("Juniper-IKE-MIB", "juniIkeSaRemaining"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIkeSaGroup = juniIkeSaGroup.setStatus('obsolete')
juniIkeSa2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 2, 5)).setObjects(("Juniper-IKE-MIB", "juniIkeSa2State"), ("Juniper-IKE-MIB", "juniIkeSa2Remaining"), ("Juniper-IKE-MIB", "juniRemoteCookie"), ("Juniper-IKE-MIB", "juniLocalCookie"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIkeSa2Group = juniIkeSa2Group.setStatus('current')
juniIkePolicyRuleV2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 71, 2, 2, 6)).setObjects(("Juniper-IKE-MIB", "juniIkePolicyRuleV2AuthMethod"), ("Juniper-IKE-MIB", "juniIkePolicyRuleV2EncryptMethod"), ("Juniper-IKE-MIB", "juniIkePolicyRuleV2PfsGroup"), ("Juniper-IKE-MIB", "juniIkePolicyRuleV2HashMethod"), ("Juniper-IKE-MIB", "juniIkePolicyRuleV2Lifetime"), ("Juniper-IKE-MIB", "juniIkePolicyRuleV2NegotiationMode"), ("Juniper-IKE-MIB", "juniIkePolicyRuleV2IpAddress"), ("Juniper-IKE-MIB", "juniIkePolicyRuleV2RouterIndex"), ("Juniper-IKE-MIB", "juniIkePolicyRuleV2RowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniIkePolicyRuleV2Group = juniIkePolicyRuleV2Group.setStatus('current')
mibBuilder.exportSymbols("Juniper-IKE-MIB", juniIkeSaRemaining=juniIkeSaRemaining, juniIkePolicyRuleV2Priority=juniIkePolicyRuleV2Priority, juniIkePolicyRuleV2AuthMethod=juniIkePolicyRuleV2AuthMethod, juniIkeSaRemotePort=juniIkeSaRemotePort, juniIkeSa2Group=juniIkeSa2Group, juniIkeSaNegotiationDone=juniIkeSaNegotiationDone, juniIkeSa2RemoteIpAddr=juniIkeSa2RemoteIpAddr, juniIkeSa2Entry=juniIkeSa2Entry, juniIkeFqdnPresharedKeyEntry=juniIkeFqdnPresharedKeyEntry, juniIkeSaState=juniIkeSaState, juniIkeSa2RouterIndex=juniIkeSa2RouterIndex, juniIkeIpv4PresharedRemoteIpAddr=juniIkeIpv4PresharedRemoteIpAddr, juniIkeSaLocalPort=juniIkeSaLocalPort, juniIkePolicyRuleLifetime=juniIkePolicyRuleLifetime, juniIkeMIB=juniIkeMIB, juniIkeSaEntry=juniIkeSaEntry, juniIkePolicyRuleEntry=juniIkePolicyRuleEntry, juniIkePolicyRuleTable=juniIkePolicyRuleTable, juniIkeSa2State=juniIkeSa2State, juniIkePolicyRuleV2PfsGroup=juniIkePolicyRuleV2PfsGroup, juniIkeCompliance3=juniIkeCompliance3, juniIkePolicyRuleV2IpAddress=juniIkePolicyRuleV2IpAddress, juniIkePolicyRuleAuthMethod=juniIkePolicyRuleAuthMethod, juniIkeSaGroup=juniIkeSaGroup, JuniIkeGroup=JuniIkeGroup, juniIkeSaLocalIpAddr=juniIkeSaLocalIpAddr, juniIkeSaRemoteIpAddr=juniIkeSaRemoteIpAddr, juniIkePolicyRuleHashMethod=juniIkePolicyRuleHashMethod, juniIkeIpv4PreSharedKeyGroup=juniIkeIpv4PreSharedKeyGroup, juniIkePolicyRuleV2HashMethod=juniIkePolicyRuleV2HashMethod, juniIke=juniIke, juniIkePolicyRuleV2RouterIndex=juniIkePolicyRuleV2RouterIndex, juniIkeFqdnPresharedKeyRowStatus=juniIkeFqdnPresharedKeyRowStatus, juniIkeSa2Table=juniIkeSa2Table, juniIkeSa2Direction=juniIkeSa2Direction, JuniIkeEncryptionMethod=JuniIkeEncryptionMethod, juniIkeIpv4PresharedMaskedKeyStr=juniIkeIpv4PresharedMaskedKeyStr, juniIkeSaTable=juniIkeSaTable, JuniIkeHashMethod=JuniIkeHashMethod, JuniIpsecPhase1SaState=JuniIpsecPhase1SaState, juniIkePolicyRuleV2NegotiationMode=juniIkePolicyRuleV2NegotiationMode, juniIkeFqdnPresharedRemote=juniIkeFqdnPresharedRemote, juniIkeMIBCompliances=juniIkeMIBCompliances, juniIkeMIBConformance=juniIkeMIBConformance, juniIkeSa2Remaining=juniIkeSa2Remaining, juniLocalCookie=juniLocalCookie, juniIkeSaRouterIndex=juniIkeSaRouterIndex, juniIkeFqdnPreSharedKeyGroup=juniIkeFqdnPreSharedKeyGroup, juniIkeIpv4PresharedKeyRowStatus=juniIkeIpv4PresharedKeyRowStatus, juniIkePolicyRulePriority=juniIkePolicyRulePriority, JuniIkeNegotiationV2Mode=JuniIkeNegotiationV2Mode, juniIkeSaDirection=juniIkeSaDirection, juniIkePolicyRuleV2Lifetime=juniIkePolicyRuleV2Lifetime, juniIkePolicyRuleGroup=juniIkePolicyRuleGroup, juniIkePolicyRuleV2Entry=juniIkePolicyRuleV2Entry, juniIkeFqdnPresharedKeyStr=juniIkeFqdnPresharedKeyStr, juniIkeFqdnPresharedMaskedKeyStr=juniIkeFqdnPresharedMaskedKeyStr, juniIkeCompliance=juniIkeCompliance, JuniIpsecPhase1SaDirection=JuniIpsecPhase1SaDirection, juniIkeSa2LocalIpAddr=juniIkeSa2LocalIpAddr, juniIkePolicyRuleV2Group=juniIkePolicyRuleV2Group, juniIkeIpv4PresharedRouterIdx=juniIkeIpv4PresharedRouterIdx, juniIkePolicyRuleV2RowStatus=juniIkePolicyRuleV2RowStatus, juniRemoteCookie=juniRemoteCookie, PYSNMP_MODULE_ID=juniIkeMIB, juniIkePolicyRuleNegotiationMode=juniIkePolicyRuleNegotiationMode, juniIkePolicyRuleEncryptMethod=juniIkePolicyRuleEncryptMethod, juniIkeIpv4PresharedKeyEntry=juniIkeIpv4PresharedKeyEntry, JuniIkeAuthenticationMethod=JuniIkeAuthenticationMethod, juniIkePolicyRuleV2Table=juniIkePolicyRuleV2Table, juniIkeFqdnPresharedKeyTable=juniIkeFqdnPresharedKeyTable, juniIkeMIBGroups=juniIkeMIBGroups, juniIkeIpv4PresharedKeyStr=juniIkeIpv4PresharedKeyStr, juniIkeFqdnPresharedRouterIndex=juniIkeFqdnPresharedRouterIndex, juniIkeIpv4PresharedKeyTable=juniIkeIpv4PresharedKeyTable, juniIkeCompliance2=juniIkeCompliance2, juniIkePolicyRulePfsGroup=juniIkePolicyRulePfsGroup, juniIkeObjects=juniIkeObjects, JuniIkeNegotiationMode=JuniIkeNegotiationMode, juniIkePolicyRuleRowStatus=juniIkePolicyRuleRowStatus, juniIkePolicyRuleV2EncryptMethod=juniIkePolicyRuleV2EncryptMethod)
