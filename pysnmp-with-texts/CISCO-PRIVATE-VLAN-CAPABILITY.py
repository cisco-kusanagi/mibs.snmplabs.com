#
# PySNMP MIB module CISCO-PRIVATE-VLAN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PRIVATE-VLAN-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:10:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, IpAddress, Gauge32, ModuleIdentity, Unsigned32, MibIdentifier, Counter64, Integer32, ObjectIdentity, Bits, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "IpAddress", "Gauge32", "ModuleIdentity", "Unsigned32", "MibIdentifier", "Counter64", "Integer32", "ObjectIdentity", "Bits", "NotificationType", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPrivateVlanCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 402))
ciscoPrivateVlanCapability.setRevisions(('2004-03-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPrivateVlanCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPrivateVlanCapability.setLastUpdated('200403310000Z')
if mibBuilder.loadTexts: ciscoPrivateVlanCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPrivateVlanCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPrivateVlanCapability.setDescription('The capabilities description of CISCO-PRIVATE-VLAN-MIB.')
cPrivateVlanCapV12R0111ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 402, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPrivateVlanCapV12R0111ECat6K = cPrivateVlanCapV12R0111ECat6K.setProductRelease('Cisco IOS 12.1(11E) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPrivateVlanCapV12R0111ECat6K = cPrivateVlanCapV12R0111ECat6K.setStatus('current')
if mibBuilder.loadTexts: cPrivateVlanCapV12R0111ECat6K.setDescription('CISCO-PRIVATE-VLAN-MIB capabilities.')
cPrivateVlanCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 402, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPrivateVlanCapCatOSV08R0101 = cPrivateVlanCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPrivateVlanCapCatOSV08R0101 = cPrivateVlanCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: cPrivateVlanCapCatOSV08R0101.setDescription('CISCO-PRIVATE-VLAN-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-PRIVATE-VLAN-CAPABILITY", cPrivateVlanCapV12R0111ECat6K=cPrivateVlanCapV12R0111ECat6K, PYSNMP_MODULE_ID=ciscoPrivateVlanCapability, cPrivateVlanCapCatOSV08R0101=cPrivateVlanCapCatOSV08R0101, ciscoPrivateVlanCapability=ciscoPrivateVlanCapability)
