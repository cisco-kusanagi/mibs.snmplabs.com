#
# PySNMP MIB module CISCO-FABRIC-MCAST-APPL-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FABRIC-MCAST-APPL-MIB-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:40:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, ModuleIdentity, Integer32, MibIdentifier, Counter32, Gauge32, Unsigned32, NotificationType, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "ModuleIdentity", "Integer32", "MibIdentifier", "Counter32", "Gauge32", "Unsigned32", "NotificationType", "TimeTicks", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFabricMcastApplCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 510))
ciscoFabricMcastApplCapability.setRevisions(('2006-06-12 00:00',))
if mibBuilder.loadTexts: ciscoFabricMcastApplCapability.setLastUpdated('200606120000Z')
if mibBuilder.loadTexts: ciscoFabricMcastApplCapability.setOrganization('Cisco Systems, Inc.')
cfmaCapabilityIOSXRV3R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 510, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmaCapabilityIOSXRV3R03 = cfmaCapabilityIOSXRV3R03.setProductRelease('Cisco IOS XR 3.3 on CRS-1 ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfmaCapabilityIOSXRV3R03 = cfmaCapabilityIOSXRV3R03.setStatus('current')
mibBuilder.exportSymbols("CISCO-FABRIC-MCAST-APPL-MIB-CAPABILITY", PYSNMP_MODULE_ID=ciscoFabricMcastApplCapability, cfmaCapabilityIOSXRV3R03=cfmaCapabilityIOSXRV3R03, ciscoFabricMcastApplCapability=ciscoFabricMcastApplCapability)
