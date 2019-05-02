#
# PySNMP MIB module CISCO-DIGITAL-MEDIA-SYSTEMS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DIGITAL-MEDIA-SYSTEMS-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:54:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ObjectIdentity, TimeTicks, Counter32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, MibIdentifier, ModuleIdentity, Unsigned32, Integer32, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "Counter32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Integer32", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDigitalMediaSystemsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 570))
ciscoDigitalMediaSystemsCapability.setRevisions(('2008-06-04 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDigitalMediaSystemsCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDigitalMediaSystemsCapability.setLastUpdated('200806040000Z')
if mibBuilder.loadTexts: ciscoDigitalMediaSystemsCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoDigitalMediaSystemsCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-dms@cisco.com')
if mibBuilder.loadTexts: ciscoDigitalMediaSystemsCapability.setDescription('The agent capabilities for CISCO-DIGITAL-MEDIA-SYSTEMS-MIB.')
ciscoDigitalMediaSystemsCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 570, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDigitalMediaSystemsCapabilityV5R00 = ciscoDigitalMediaSystemsCapabilityV5R00.setProductRelease('DMS Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDigitalMediaSystemsCapabilityV5R00 = ciscoDigitalMediaSystemsCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoDigitalMediaSystemsCapabilityV5R00.setDescription('Agent capabilities for DMS in Release 5.0.0.')
mibBuilder.exportSymbols("CISCO-DIGITAL-MEDIA-SYSTEMS-CAPABILITY", ciscoDigitalMediaSystemsCapability=ciscoDigitalMediaSystemsCapability, PYSNMP_MODULE_ID=ciscoDigitalMediaSystemsCapability, ciscoDigitalMediaSystemsCapabilityV5R00=ciscoDigitalMediaSystemsCapabilityV5R00)
