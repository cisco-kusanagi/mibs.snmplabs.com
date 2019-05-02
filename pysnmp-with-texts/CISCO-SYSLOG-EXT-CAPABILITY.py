#
# PySNMP MIB module CISCO-SYSLOG-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SYSLOG-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:13:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, Gauge32, Bits, ModuleIdentity, TimeTicks, Unsigned32, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "Gauge32", "Bits", "ModuleIdentity", "TimeTicks", "Unsigned32", "MibIdentifier", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSyslogExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 454))
ciscoSyslogExtCapability.setRevisions(('2008-06-30 00:00', '2006-04-18 00:00', '2005-09-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSyslogExtCapability.setRevisionsDescriptions(('Added ciscoSyslogExtCapabilityc4710aceVA1R700 agent capabilities for ACE 4710 Application Control Engine Appliance. Obsoleted ciscoSyslogExtCapabilityACSWV03R0000 for Application Control Engine(ACE) module, as VARIATION description for some of the objects was missing. Added ciscoSyslogExtCapACSWV03R0000Rev1 for Application Control Engine(ACE) module.', 'Added ciscoSyslogExtCapabilityACSWV03R0000 for Application Control Engine(ACE) module.', 'Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoSyslogExtCapability.setLastUpdated('200806300000Z')
if mibBuilder.loadTexts: ciscoSyslogExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSyslogExtCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoSyslogExtCapability.setDescription('Agent capabilities for CISCO-SYSLOG-EXT-MIB.')
ciscoSyslogExtCapabilityMDS3R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 454, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityMDS3R0 = ciscoSyslogExtCapabilityMDS3R0.setProductRelease('Cisco MDS 3.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityMDS3R0 = ciscoSyslogExtCapabilityMDS3R0.setStatus('current')
if mibBuilder.loadTexts: ciscoSyslogExtCapabilityMDS3R0.setDescription('Cisco SYSLOG EXTENSION MIB capabilities')
ciscoSyslogExtCapabilityACSWV03R0000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 454, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityACSWV03R0000 = ciscoSyslogExtCapabilityACSWV03R0000.setProductRelease('ACSW (Application Control Software) 3.0\n                for Application Control Engine(ACE) module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityACSWV03R0000 = ciscoSyslogExtCapabilityACSWV03R0000.setStatus('obsolete')
if mibBuilder.loadTexts: ciscoSyslogExtCapabilityACSWV03R0000.setDescription('CISCO-SYSLOG-EXT-MIB capabilities.')
ciscoSyslogExtCapACSWV03R0000Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 454, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapACSWV03R0000Rev1 = ciscoSyslogExtCapACSWV03R0000Rev1.setProductRelease('ACSW (Application Control Software) 3.0\n                    for Application Control Engine(ACE) module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapACSWV03R0000Rev1 = ciscoSyslogExtCapACSWV03R0000Rev1.setStatus('current')
if mibBuilder.loadTexts: ciscoSyslogExtCapACSWV03R0000Rev1.setDescription('CISCO-SYSLOG-EXT-MIB capabilities.')
ciscoSyslogExtCapabilityc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 454, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityc4710aceVA1R700 = ciscoSyslogExtCapabilityc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityc4710aceVA1R700 = ciscoSyslogExtCapabilityc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoSyslogExtCapabilityc4710aceVA1R700.setDescription('CISCO-SYSLOG-EXT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SYSLOG-EXT-CAPABILITY", ciscoSyslogExtCapACSWV03R0000Rev1=ciscoSyslogExtCapACSWV03R0000Rev1, ciscoSyslogExtCapabilityc4710aceVA1R700=ciscoSyslogExtCapabilityc4710aceVA1R700, ciscoSyslogExtCapabilityACSWV03R0000=ciscoSyslogExtCapabilityACSWV03R0000, ciscoSyslogExtCapability=ciscoSyslogExtCapability, ciscoSyslogExtCapabilityMDS3R0=ciscoSyslogExtCapabilityMDS3R0, PYSNMP_MODULE_ID=ciscoSyslogExtCapability)
