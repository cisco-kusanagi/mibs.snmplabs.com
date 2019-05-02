#
# PySNMP MIB module JUNIPER-MAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-MAC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:00:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Bits, Gauge32, ObjectIdentity, Unsigned32, NotificationType, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, IpAddress, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "Gauge32", "ObjectIdentity", "Unsigned32", "NotificationType", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "IpAddress", "iso", "Counter64")
DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress")
jnxMac = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 23))
jnxMac.setRevisions(('2002-10-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxMac.setRevisionsDescriptions(('MacStats MIB added.',))
if mibBuilder.loadTexts: jnxMac.setLastUpdated('200307182153Z')
if mibBuilder.loadTexts: jnxMac.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxMac.setContactInfo(' Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net')
if mibBuilder.loadTexts: jnxMac.setDescription("This is Juniper Networks' implementation of enterprise specific MIB for Ethernet Mac Stats")
class JnxVlanIndex(TextualConvention, Unsigned32):
    description = 'A value used to index per-VLAN tables. A values of 0 is not permitted. The value of 4095 is reserved for untagged interfaces; if the value is between 1 and 4094 inclusive, it represents an IEEE 802.1Q VLAN-ID with global scope within a given bridged domain (see VlanId textual convention). If the value is greater than 4095 then it represents a VLAN with scope local to the particular agent, i.e. one without a global VLAN-ID assigned to it. Such VLANs are outside the scope of IEEE 802.1Q but it is convenient to be able to manage them in the same way using this MIB.'
    status = 'current'

jnxMacStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1))
jnxMacStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1), )
if mibBuilder.loadTexts: jnxMacStatsTable.setStatus('current')
if mibBuilder.loadTexts: jnxMacStatsTable.setDescription('a list of MacStats entry for GE ethernet interfaces')
jnxMacStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "JUNIPER-MAC-MIB", "jnxVlanIndex"), (0, "JUNIPER-MAC-MIB", "jnxSourceMacAddress"))
if mibBuilder.loadTexts: jnxMacStatsEntry.setStatus('current')
if mibBuilder.loadTexts: jnxMacStatsEntry.setDescription('An entry containing statistics information applicable to a particular GE ethernet interfaces.')
jnxVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 1), JnxVlanIndex())
if mibBuilder.loadTexts: jnxVlanIndex.setStatus('current')
if mibBuilder.loadTexts: jnxVlanIndex.setDescription('The VLAN ID refering to this VLAN.')
jnxSourceMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 2), MacAddress())
if mibBuilder.loadTexts: jnxSourceMacAddress.setStatus('current')
if mibBuilder.loadTexts: jnxSourceMacAddress.setDescription('The Source MAC address.')
jnxMacHCInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMacHCInOctets.setStatus('current')
if mibBuilder.loadTexts: jnxMacHCInOctets.setDescription('The number of total octets received in this VLAN/MAC Address.')
jnxMacHCInFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMacHCInFrames.setStatus('current')
if mibBuilder.loadTexts: jnxMacHCInFrames.setDescription('The number of total frames received in this VLAN/MAC Address.')
jnxMacHCOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMacHCOutOctets.setStatus('current')
if mibBuilder.loadTexts: jnxMacHCOutOctets.setDescription('The number of total octets transmitted in this VLAN/MAC Address.')
jnxMacHCOutFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 23, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxMacHCOutFrames.setStatus('current')
if mibBuilder.loadTexts: jnxMacHCOutFrames.setDescription('The number of total frames transmitted in this VLAN/MAC Address.')
mibBuilder.exportSymbols("JUNIPER-MAC-MIB", jnxMacHCOutOctets=jnxMacHCOutOctets, jnxMacHCInFrames=jnxMacHCInFrames, JnxVlanIndex=JnxVlanIndex, jnxSourceMacAddress=jnxSourceMacAddress, jnxMacStatsTable=jnxMacStatsTable, jnxVlanIndex=jnxVlanIndex, PYSNMP_MODULE_ID=jnxMac, jnxMacHCInOctets=jnxMacHCInOctets, jnxMacHCOutFrames=jnxMacHCOutFrames, jnxMacStats=jnxMacStats, jnxMacStatsEntry=jnxMacStatsEntry, jnxMac=jnxMac)
