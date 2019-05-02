#
# PySNMP MIB module CISCO-SYSLOG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SYSLOG-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:13:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Counter64, Bits, Integer32, TimeTicks, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, ModuleIdentity, NotificationType, Gauge32, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Integer32", "TimeTicks", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "NotificationType", "Gauge32", "Counter32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSyslogCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 61))
ciscoSyslogCapability.setRevisions(('2010-01-22 14:32', '2008-08-11 00:00', '2008-06-08 00:00', '2006-10-26 00:00', '2006-05-25 00:00', '2004-02-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSyslogCapability.setRevisionsDescriptions(('Added capability for Visual Quality Experience Server (VQE-S) and Visual Quality Experience Tools (VQE-TOOLS) platforms.', 'Adding newlines at the end of the MIB file.', 'Added Agent capability for ACE 4710 Application Control Engine Appliance.', 'Added capability for Cisco TelePresence System (CTS) and Cisco TelePresence Manager (CTM) platforms.', 'Added Agent capability ciscoSyslogCapACSWV03R000 for Application Control Engine (ACE).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSyslogCapability.setLastUpdated('201001221432Z')
if mibBuilder.loadTexts: ciscoSyslogCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSyslogCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSyslogCapability.setDescription('The capabilities description of CISCO-SYSLOG-MIB.')
ciscoSyslogCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCatOSV08R0101 = ciscoSyslogCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCatOSV08R0101 = ciscoSyslogCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoSyslogCapCatOSV08R0101.setDescription('CISCO-SYSLOG-MIB capabilities.')
ciscoSyslogCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapACSWV03R000 = ciscoSyslogCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n \n                   for Application Control Engine(ACE)\n\n                    Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapACSWV03R000 = ciscoSyslogCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoSyslogCapACSWV03R000.setDescription('CISCO-SYSLOG-MIB capabilities.')
ciscoSyslogCapCTSV100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCTSV100 = ciscoSyslogCapCTSV100.setProductRelease('Cisco TelePresence System (CTS) 1.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCTSV100 = ciscoSyslogCapCTSV100.setStatus('current')
if mibBuilder.loadTexts: ciscoSyslogCapCTSV100.setDescription('CISCO-SYSLOG-MIB capabilities.')
ciscoSyslogCapCTMV1000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCTMV1000 = ciscoSyslogCapCTMV1000.setProductRelease('Cisco TelePresence Manager (CTM) 1.0.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCTMV1000 = ciscoSyslogCapCTMV1000.setStatus('current')
if mibBuilder.loadTexts: ciscoSyslogCapCTMV1000.setDescription('CISCO-SYSLOG-MIB capabilities.')
ciscoSyslogCapc4710aceVA1R70 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapc4710aceVA1R70 = ciscoSyslogCapc4710aceVA1R70.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapc4710aceVA1R70 = ciscoSyslogCapc4710aceVA1R70.setStatus('current')
if mibBuilder.loadTexts: ciscoSyslogCapc4710aceVA1R70.setDescription('CISCO-SYSLOG-MIB capabilities.')
ciscoSyslogCapVqe = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapVqe = ciscoSyslogCapVqe.setProductRelease('VQE 3.5 release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapVqe = ciscoSyslogCapVqe.setStatus('current')
if mibBuilder.loadTexts: ciscoSyslogCapVqe.setDescription('CISCO-SYSLOG-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SYSLOG-CAPABILITY", ciscoSyslogCapability=ciscoSyslogCapability, PYSNMP_MODULE_ID=ciscoSyslogCapability, ciscoSyslogCapCatOSV08R0101=ciscoSyslogCapCatOSV08R0101, ciscoSyslogCapVqe=ciscoSyslogCapVqe, ciscoSyslogCapACSWV03R000=ciscoSyslogCapACSWV03R000, ciscoSyslogCapCTMV1000=ciscoSyslogCapCTMV1000, ciscoSyslogCapc4710aceVA1R70=ciscoSyslogCapc4710aceVA1R70, ciscoSyslogCapCTSV100=ciscoSyslogCapCTSV100)
