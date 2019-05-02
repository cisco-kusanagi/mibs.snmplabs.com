#
# PySNMP MIB module CISCO-FABRIC-HFR-MIB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FABRIC-HFR-MIB-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:57:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Bits, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, Counter64, Counter32, NotificationType, Gauge32, Unsigned32, Integer32, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "Counter64", "Counter32", "NotificationType", "Gauge32", "Unsigned32", "Integer32", "MibIdentifier", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFabricHfrCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 511))
ciscoFabricHfrCapability.setRevisions(('2006-06-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFabricHfrCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoFabricHfrCapability.setLastUpdated('200606120000Z')
if mibBuilder.loadTexts: ciscoFabricHfrCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoFabricHfrCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-fabric@cisco.com')
if mibBuilder.loadTexts: ciscoFabricHfrCapability.setDescription('The capabilities description of CISCO-FABRIC-HFR-MIB.')
cfhCapabilityIOSXRV3R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 511, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfhCapabilityIOSXRV3R03 = cfhCapabilityIOSXRV3R03.setProductRelease('Cisco IOS XR 3.3 on CRS-1 ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfhCapabilityIOSXRV3R03 = cfhCapabilityIOSXRV3R03.setStatus('current')
if mibBuilder.loadTexts: cfhCapabilityIOSXRV3R03.setDescription('CISCO-FABRIC-HFR-MIB capabilities for IOS XR release 3.3')
mibBuilder.exportSymbols("CISCO-FABRIC-HFR-MIB-CAPABILITY", cfhCapabilityIOSXRV3R03=cfhCapabilityIOSXRV3R03, ciscoFabricHfrCapability=ciscoFabricHfrCapability, PYSNMP_MODULE_ID=ciscoFabricHfrCapability)
