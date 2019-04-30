#
# PySNMP MIB module CISCO-CONTENT-SERVICES-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CONTENT-SERVICES-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:36:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, Gauge32, TimeTicks, IpAddress, NotificationType, iso, Counter32, Bits, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "Gauge32", "TimeTicks", "IpAddress", "NotificationType", "iso", "Counter32", "Bits", "ModuleIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoContentServicesCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 581))
ciscoContentServicesCapability.setRevisions(('2010-12-23 00:00', '2010-02-11 00:00', '2009-08-21 00:00', '2009-05-09 00:00',))
if mibBuilder.loadTexts: ciscoContentServicesCapability.setLastUpdated('201012230000Z')
if mibBuilder.loadTexts: ciscoContentServicesCapability.setOrganization('Cisco Systems, Inc.')
ciscoContentServicesCapabilityAdcV01R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityAdcV01R00 = ciscoContentServicesCapabilityAdcV01R00.setProductRelease('Cisco IOS 12.4MF')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityAdcV01R00 = ciscoContentServicesCapabilityAdcV01R00.setStatus('current')
ciscoContentServicesCapabilityCSG2R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R03 = ciscoContentServicesCapabilityCSG2R03.setProductRelease('Cisco IOS 12.4(22)MD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R03 = ciscoContentServicesCapabilityCSG2R03.setStatus('current')
ciscoContentServicesCapabilityCSG2R0305 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R0305 = ciscoContentServicesCapabilityCSG2R0305.setProductRelease('Cisco IOS 12.4(22)MDA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R0305 = ciscoContentServicesCapabilityCSG2R0305.setStatus('current')
ciscoContentServicesCapabilityCSG2R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R04 = ciscoContentServicesCapabilityCSG2R04.setProductRelease('Cisco IOS 12.4(24)MD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R04 = ciscoContentServicesCapabilityCSG2R04.setStatus('current')
ciscoContentServicesCapabilityCSG2R06 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R06 = ciscoContentServicesCapabilityCSG2R06.setProductRelease('Cisco IOS R6')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R06 = ciscoContentServicesCapabilityCSG2R06.setStatus('current')
mibBuilder.exportSymbols("CISCO-CONTENT-SERVICES-CAPABILITY", ciscoContentServicesCapability=ciscoContentServicesCapability, ciscoContentServicesCapabilityCSG2R03=ciscoContentServicesCapabilityCSG2R03, ciscoContentServicesCapabilityCSG2R06=ciscoContentServicesCapabilityCSG2R06, ciscoContentServicesCapabilityCSG2R04=ciscoContentServicesCapabilityCSG2R04, ciscoContentServicesCapabilityAdcV01R00=ciscoContentServicesCapabilityAdcV01R00, PYSNMP_MODULE_ID=ciscoContentServicesCapability, ciscoContentServicesCapabilityCSG2R0305=ciscoContentServicesCapabilityCSG2R0305)
