#
# PySNMP MIB module JUNIPER-JS-IPSEC-VPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-JS-IPSEC-VPN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:48:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
jnxIpSecTunnelMonEntry, = mibBuilder.importSymbols("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunnelMonEntry")
jnxJsIPSecVpn, = mibBuilder.importSymbols("JUNIPER-JS-SMI", "jnxJsIPSecVpn")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, TimeTicks, Counter64, Unsigned32, Integer32, ObjectIdentity, MibIdentifier, ModuleIdentity, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "TimeTicks", "Counter64", "Unsigned32", "Integer32", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Bits", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxJsIpSecVpnMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1))
jnxJsIpSecVpnMib.setRevisions(('2007-04-27 00:00',))
if mibBuilder.loadTexts: jnxJsIpSecVpnMib.setLastUpdated('200705112153Z')
if mibBuilder.loadTexts: jnxJsIpSecVpnMib.setOrganization('Juniper Networks, Inc.')
jnxJsIpSecVpnNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 0))
jnxJsIpSecVpnPhaseOne = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 1))
jnxJsIpSecVpnPhaseTwo = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2))
class JnxJsIpSecVpnType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("policyBased", 1), ("routeBased", 2))

jnxJsIpSecTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1), )
if mibBuilder.loadTexts: jnxJsIpSecTunnelTable.setStatus('current')
jnxJsIpSecTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1, 1), )
jnxIpSecTunnelMonEntry.registerAugmentions(("JUNIPER-JS-IPSEC-VPN-MIB", "jnxJsIpSecTunnelEntry"))
jnxJsIpSecTunnelEntry.setIndexNames(*jnxIpSecTunnelMonEntry.getIndexNames())
if mibBuilder.loadTexts: jnxJsIpSecTunnelEntry.setStatus('current')
jnxJsIpSecTunPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsIpSecTunPolicyName.setStatus('current')
jnxJsIpSecVpnTunType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1, 1, 2), JnxJsIpSecVpnType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsIpSecVpnTunType.setStatus('current')
jnxJsIpSecTunCfgMonState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsIpSecTunCfgMonState.setStatus('current')
jnxJsIpSecTunState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("vpnMonitoringDisabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsIpSecTunState.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-JS-IPSEC-VPN-MIB", jnxJsIpSecVpnMib=jnxJsIpSecVpnMib, jnxJsIpSecTunState=jnxJsIpSecTunState, jnxJsIpSecVpnPhaseOne=jnxJsIpSecVpnPhaseOne, JnxJsIpSecVpnType=JnxJsIpSecVpnType, PYSNMP_MODULE_ID=jnxJsIpSecVpnMib, jnxJsIpSecTunCfgMonState=jnxJsIpSecTunCfgMonState, jnxJsIpSecTunnelEntry=jnxJsIpSecTunnelEntry, jnxJsIpSecVpnNotifications=jnxJsIpSecVpnNotifications, jnxJsIpSecVpnPhaseTwo=jnxJsIpSecVpnPhaseTwo, jnxJsIpSecTunnelTable=jnxJsIpSecTunnelTable, jnxJsIpSecTunPolicyName=jnxJsIpSecTunPolicyName, jnxJsIpSecVpnTunType=jnxJsIpSecVpnTunType)
