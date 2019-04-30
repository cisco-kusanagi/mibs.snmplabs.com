#
# PySNMP MIB module CISCO-FABRIC-HFR-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FABRIC-HFR-MIB-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:40:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
TimeTicks, Counter32, MibIdentifier, NotificationType, iso, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, Counter64, Bits, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "MibIdentifier", "NotificationType", "iso", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "Counter64", "Bits", "Unsigned32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoFabricHfrCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 511))
ciscoFabricHfrCapability.setRevisions(('2006-06-12 00:00',))
if mibBuilder.loadTexts: ciscoFabricHfrCapability.setLastUpdated('200606120000Z')
if mibBuilder.loadTexts: ciscoFabricHfrCapability.setOrganization('Cisco Systems, Inc.')
cfhCapabilityIOSXRV3R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 511, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfhCapabilityIOSXRV3R03 = cfhCapabilityIOSXRV3R03.setProductRelease('Cisco IOS XR 3.3 on CRS-1 ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfhCapabilityIOSXRV3R03 = cfhCapabilityIOSXRV3R03.setStatus('current')
mibBuilder.exportSymbols("CISCO-FABRIC-HFR-MIB-CAPABILITY", PYSNMP_MODULE_ID=ciscoFabricHfrCapability, ciscoFabricHfrCapability=ciscoFabricHfrCapability, cfhCapabilityIOSXRV3R03=cfhCapabilityIOSXRV3R03)
