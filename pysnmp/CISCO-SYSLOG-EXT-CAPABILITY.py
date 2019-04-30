#
# PySNMP MIB module CISCO-SYSLOG-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SYSLOG-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:57:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, ObjectIdentity, MibIdentifier, Counter32, TimeTicks, Integer32, Gauge32, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "MibIdentifier", "Counter32", "TimeTicks", "Integer32", "Gauge32", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "Unsigned32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSyslogExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 454))
ciscoSyslogExtCapability.setRevisions(('2008-06-30 00:00', '2006-04-18 00:00', '2005-09-01 00:00',))
if mibBuilder.loadTexts: ciscoSyslogExtCapability.setLastUpdated('200806300000Z')
if mibBuilder.loadTexts: ciscoSyslogExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoSyslogExtCapabilityMDS3R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 454, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityMDS3R0 = ciscoSyslogExtCapabilityMDS3R0.setProductRelease('Cisco MDS 3.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityMDS3R0 = ciscoSyslogExtCapabilityMDS3R0.setStatus('current')
ciscoSyslogExtCapabilityACSWV03R0000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 454, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityACSWV03R0000 = ciscoSyslogExtCapabilityACSWV03R0000.setProductRelease('ACSW (Application Control Software) 3.0\n                for Application Control Engine(ACE) module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityACSWV03R0000 = ciscoSyslogExtCapabilityACSWV03R0000.setStatus('obsolete')
ciscoSyslogExtCapACSWV03R0000Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 454, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapACSWV03R0000Rev1 = ciscoSyslogExtCapACSWV03R0000Rev1.setProductRelease('ACSW (Application Control Software) 3.0\n                    for Application Control Engine(ACE) module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapACSWV03R0000Rev1 = ciscoSyslogExtCapACSWV03R0000Rev1.setStatus('current')
ciscoSyslogExtCapabilityc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 454, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityc4710aceVA1R700 = ciscoSyslogExtCapabilityc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogExtCapabilityc4710aceVA1R700 = ciscoSyslogExtCapabilityc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYSLOG-EXT-CAPABILITY", ciscoSyslogExtCapabilityMDS3R0=ciscoSyslogExtCapabilityMDS3R0, ciscoSyslogExtCapabilityACSWV03R0000=ciscoSyslogExtCapabilityACSWV03R0000, PYSNMP_MODULE_ID=ciscoSyslogExtCapability, ciscoSyslogExtCapabilityc4710aceVA1R700=ciscoSyslogExtCapabilityc4710aceVA1R700, ciscoSyslogExtCapability=ciscoSyslogExtCapability, ciscoSyslogExtCapACSWV03R0000Rev1=ciscoSyslogExtCapACSWV03R0000Rev1)
