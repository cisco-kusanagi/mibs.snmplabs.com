#
# PySNMP MIB module CISCO-PRIVATE-VLAN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-PRIVATE-VLAN-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:53:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Counter32, Counter64, ModuleIdentity, Integer32, iso, MibIdentifier, ObjectIdentity, Gauge32, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "ModuleIdentity", "Integer32", "iso", "MibIdentifier", "ObjectIdentity", "Gauge32", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoPrivateVlanCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 402))
ciscoPrivateVlanCapability.setRevisions(('2004-03-31 00:00',))
if mibBuilder.loadTexts: ciscoPrivateVlanCapability.setLastUpdated('200403310000Z')
if mibBuilder.loadTexts: ciscoPrivateVlanCapability.setOrganization('Cisco Systems, Inc.')
cPrivateVlanCapV12R0111ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 402, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPrivateVlanCapV12R0111ECat6K = cPrivateVlanCapV12R0111ECat6K.setProductRelease('Cisco IOS 12.1(11E) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPrivateVlanCapV12R0111ECat6K = cPrivateVlanCapV12R0111ECat6K.setStatus('current')
cPrivateVlanCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 402, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPrivateVlanCapCatOSV08R0101 = cPrivateVlanCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPrivateVlanCapCatOSV08R0101 = cPrivateVlanCapCatOSV08R0101.setStatus('current')
mibBuilder.exportSymbols("CISCO-PRIVATE-VLAN-CAPABILITY", PYSNMP_MODULE_ID=ciscoPrivateVlanCapability, cPrivateVlanCapCatOSV08R0101=cPrivateVlanCapCatOSV08R0101, ciscoPrivateVlanCapability=ciscoPrivateVlanCapability, cPrivateVlanCapV12R0111ECat6K=cPrivateVlanCapV12R0111ECat6K)
