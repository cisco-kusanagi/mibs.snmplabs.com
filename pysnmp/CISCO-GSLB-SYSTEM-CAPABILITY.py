#
# PySNMP MIB module CISCO-GSLB-SYSTEM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-GSLB-SYSTEM-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:42:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, Counter64, Unsigned32, Gauge32, Counter32, ObjectIdentity, Bits, IpAddress, ModuleIdentity, iso, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "Counter64", "Unsigned32", "Gauge32", "Counter32", "ObjectIdentity", "Bits", "IpAddress", "ModuleIdentity", "iso", "NotificationType", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoGslbSystemCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 534))
ciscoGslbSystemCapability.setRevisions(('2011-09-14 00:00', '2008-09-15 00:00', '2007-02-23 00:00',))
if mibBuilder.loadTexts: ciscoGslbSystemCapability.setLastUpdated('201109140000Z')
if mibBuilder.loadTexts: ciscoGslbSystemCapability.setOrganization('Cisco Systems, Inc.')
ciscoGslbSystemCapabilityV02R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 534, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV02R00 = ciscoGslbSystemCapabilityV02R00.setProductRelease('GSS 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV02R00 = ciscoGslbSystemCapabilityV02R00.setStatus('current')
ciscoGslbSystemCapabilityV03R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 534, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV03R00 = ciscoGslbSystemCapabilityV03R00.setProductRelease('Global Site Selector(GSS) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV03R00 = ciscoGslbSystemCapabilityV03R00.setStatus('current')
ciscoGslbSystemCapabilityV04R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 534, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV04R01 = ciscoGslbSystemCapabilityV04R01.setProductRelease('Global Site Selector(GSS) 4.1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV04R01 = ciscoGslbSystemCapabilityV04R01.setStatus('current')
mibBuilder.exportSymbols("CISCO-GSLB-SYSTEM-CAPABILITY", PYSNMP_MODULE_ID=ciscoGslbSystemCapability, ciscoGslbSystemCapabilityV03R00=ciscoGslbSystemCapabilityV03R00, ciscoGslbSystemCapability=ciscoGslbSystemCapability, ciscoGslbSystemCapabilityV02R00=ciscoGslbSystemCapabilityV02R00, ciscoGslbSystemCapabilityV04R01=ciscoGslbSystemCapabilityV04R01)
