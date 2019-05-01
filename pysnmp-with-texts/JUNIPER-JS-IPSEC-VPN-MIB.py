#
# PySNMP MIB module JUNIPER-JS-IPSEC-VPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-JS-IPSEC-VPN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:59:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
jnxIpSecTunnelMonEntry, = mibBuilder.importSymbols("JUNIPER-IPSEC-FLOW-MON-MIB", "jnxIpSecTunnelMonEntry")
jnxJsIPSecVpn, = mibBuilder.importSymbols("JUNIPER-JS-SMI", "jnxJsIPSecVpn")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, IpAddress, Counter64, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, NotificationType, iso, Unsigned32, MibIdentifier, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "Counter64", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "NotificationType", "iso", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxJsIpSecVpnMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1))
jnxJsIpSecVpnMib.setRevisions(('2007-04-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxJsIpSecVpnMib.setRevisionsDescriptions(('Create the jnxJsIpSecTunnelTable as an augmented table to the jnxIpSecTunnelMonTable in JUNIPER-IPSEC-FLOW-MON-MIB.',))
if mibBuilder.loadTexts: jnxJsIpSecVpnMib.setLastUpdated('200705112153Z')
if mibBuilder.loadTexts: jnxJsIpSecVpnMib.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxJsIpSecVpnMib.setContactInfo('Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net')
if mibBuilder.loadTexts: jnxJsIpSecVpnMib.setDescription("This module defines the object used to monitor the entries pertaining to IPSec objects and the management of the IPSEC VPN functionalities for Juniper security product lines. This mib module extend Juniper's common IPSEC flow monitoring MIB, building on the existing common infrastruature, the security implementation integrates the value-added features for the security products")
jnxJsIpSecVpnNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 0))
jnxJsIpSecVpnPhaseOne = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 1))
jnxJsIpSecVpnPhaseTwo = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2))
class JnxJsIpSecVpnType(TextualConvention, Integer32):
    description = "The type of the remote peer gateway (endpoint). It can be one of the following two types: - policyBased : tunnels requires a policy with action 'tunnel' to trigger IPSEC VPN. The device receives traffic and matches it with policy that has action 'tunnel', it performs the encryption/decryption and authentication options negotiated for this VPN phase 2 negotiation. - routeBased : requires a tunnel interface a route directing traffic to protected networks to exit the system using that tunnel interface. The tunnel interface is bound to a Phase 2 VPN configuration that specifies all the tunnel parameters. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("policyBased", 1), ("routeBased", 2))

jnxJsIpSecTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1), )
if mibBuilder.loadTexts: jnxJsIpSecTunnelTable.setStatus('current')
if mibBuilder.loadTexts: jnxJsIpSecTunnelTable.setDescription('The IPsec Phase-2 Tunnel Table. There is one entry in this table for each active IPsec Phase-2 Tunnel. If the tunnel is terminated, then the entry is no longer available after the table has been refreshed. ')
jnxJsIpSecTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1, 1), )
jnxIpSecTunnelMonEntry.registerAugmentions(("JUNIPER-JS-IPSEC-VPN-MIB", "jnxJsIpSecTunnelEntry"))
jnxJsIpSecTunnelEntry.setIndexNames(*jnxIpSecTunnelMonEntry.getIndexNames())
if mibBuilder.loadTexts: jnxJsIpSecTunnelEntry.setStatus('current')
if mibBuilder.loadTexts: jnxJsIpSecTunnelEntry.setDescription('Each entry contains the attributes associated with an active IPsec Phase-2 Tunnel.')
jnxJsIpSecTunPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsIpSecTunPolicyName.setStatus('current')
if mibBuilder.loadTexts: jnxJsIpSecTunPolicyName.setDescription('The policy name assoicated with this tunnel if the this IPSEC VPN is policy based. Otherwise, this attribute is not applicable.')
jnxJsIpSecVpnTunType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1, 1, 2), JnxJsIpSecVpnType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsIpSecVpnTunType.setStatus('current')
if mibBuilder.loadTexts: jnxJsIpSecVpnTunType.setDescription('This attribute indicates the IPSEC VPN tunnel is policy based or route based.')
jnxJsIpSecTunCfgMonState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsIpSecTunCfgMonState.setStatus('current')
if mibBuilder.loadTexts: jnxJsIpSecTunCfgMonState.setDescription('The user configuration states whether to monitor the IPSec tunnel to be alive or not. ')
jnxJsIpSecTunState = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 5, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("vpnMonitoringDisabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxJsIpSecTunState.setStatus('current')
if mibBuilder.loadTexts: jnxJsIpSecTunState.setDescription('This attribute indicates whether the IPSec Tunnel is up or down, determined by icmp ping if the jnxJsIpSecTunCfgMonState is enable. Down: VPN monitor detects the tunnel is down Up: VPN monitor detects the tunnel is up. vpnMonitoringDisabled: user has disabled VPN tunnel monitoring.')
mibBuilder.exportSymbols("JUNIPER-JS-IPSEC-VPN-MIB", jnxJsIpSecVpnPhaseOne=jnxJsIpSecVpnPhaseOne, jnxJsIpSecTunnelEntry=jnxJsIpSecTunnelEntry, jnxJsIpSecTunCfgMonState=jnxJsIpSecTunCfgMonState, jnxJsIpSecTunState=jnxJsIpSecTunState, JnxJsIpSecVpnType=JnxJsIpSecVpnType, jnxJsIpSecTunnelTable=jnxJsIpSecTunnelTable, jnxJsIpSecVpnMib=jnxJsIpSecVpnMib, jnxJsIpSecVpnPhaseTwo=jnxJsIpSecVpnPhaseTwo, PYSNMP_MODULE_ID=jnxJsIpSecVpnMib, jnxJsIpSecTunPolicyName=jnxJsIpSecTunPolicyName, jnxJsIpSecVpnTunType=jnxJsIpSecVpnTunType, jnxJsIpSecVpnNotifications=jnxJsIpSecVpnNotifications)
