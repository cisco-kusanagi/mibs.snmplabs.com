#
# PySNMP MIB module CISCO-DIGITAL-MEDIA-SYSTEMS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DIGITAL-MEDIA-SYSTEMS-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:37:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Gauge32, ObjectIdentity, MibIdentifier, Integer32, ModuleIdentity, Counter32, Bits, Unsigned32, TimeTicks, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Gauge32", "ObjectIdentity", "MibIdentifier", "Integer32", "ModuleIdentity", "Counter32", "Bits", "Unsigned32", "TimeTicks", "NotificationType", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDigitalMediaSystemsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 570))
ciscoDigitalMediaSystemsCapability.setRevisions(('2008-06-04 00:00',))
if mibBuilder.loadTexts: ciscoDigitalMediaSystemsCapability.setLastUpdated('200806040000Z')
if mibBuilder.loadTexts: ciscoDigitalMediaSystemsCapability.setOrganization('Cisco Systems, Inc.')
ciscoDigitalMediaSystemsCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 570, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDigitalMediaSystemsCapabilityV5R00 = ciscoDigitalMediaSystemsCapabilityV5R00.setProductRelease('DMS Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDigitalMediaSystemsCapabilityV5R00 = ciscoDigitalMediaSystemsCapabilityV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-DIGITAL-MEDIA-SYSTEMS-CAPABILITY", ciscoDigitalMediaSystemsCapabilityV5R00=ciscoDigitalMediaSystemsCapabilityV5R00, ciscoDigitalMediaSystemsCapability=ciscoDigitalMediaSystemsCapability, PYSNMP_MODULE_ID=ciscoDigitalMediaSystemsCapability)
