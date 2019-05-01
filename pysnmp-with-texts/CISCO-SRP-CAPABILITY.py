#
# PySNMP MIB module CISCO-SRP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SRP-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:12:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter32, iso, NotificationType, ModuleIdentity, Bits, ObjectIdentity, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Counter64, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "NotificationType", "ModuleIdentity", "Bits", "ObjectIdentity", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Counter64", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSrpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
if mibBuilder.loadTexts: ciscoSrpCapability.setLastUpdated('200005260000Z')
if mibBuilder.loadTexts: ciscoSrpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSrpCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSrpCapability.setDescription('Initial version of this MIB module.')
ciscoSrpCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSrpCapabilityV12R00 = ciscoSrpCapabilityV12R00.setProductRelease('Cisco IOS 12.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSrpCapabilityV12R00 = ciscoSrpCapabilityV12R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSrpCapabilityV12R00.setDescription('CISCO-SRP-MIB agent capabilities')
mibBuilder.exportSymbols("CISCO-SRP-CAPABILITY", ciscoSrpCapabilityV12R00=ciscoSrpCapabilityV12R00, ciscoSrpCapability=ciscoSrpCapability, PYSNMP_MODULE_ID=ciscoSrpCapability)
