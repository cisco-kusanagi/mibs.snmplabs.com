#
# PySNMP MIB module CISCO-SYSLOG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SYSLOG-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:57:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
IpAddress, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, MibIdentifier, iso, TimeTicks, Gauge32, Bits, ObjectIdentity, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "MibIdentifier", "iso", "TimeTicks", "Gauge32", "Bits", "ObjectIdentity", "Unsigned32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSyslogCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 61))
ciscoSyslogCapability.setRevisions(('2010-01-22 14:32', '2008-08-11 00:00', '2008-06-08 00:00', '2006-10-26 00:00', '2006-05-25 00:00', '2004-02-03 00:00',))
if mibBuilder.loadTexts: ciscoSyslogCapability.setLastUpdated('201001221432Z')
if mibBuilder.loadTexts: ciscoSyslogCapability.setOrganization('Cisco Systems, Inc.')
ciscoSyslogCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCatOSV08R0101 = ciscoSyslogCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCatOSV08R0101 = ciscoSyslogCapCatOSV08R0101.setStatus('current')
ciscoSyslogCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapACSWV03R000 = ciscoSyslogCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n \n                   for Application Control Engine(ACE)\n\n                    Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapACSWV03R000 = ciscoSyslogCapACSWV03R000.setStatus('current')
ciscoSyslogCapCTSV100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCTSV100 = ciscoSyslogCapCTSV100.setProductRelease('Cisco TelePresence System (CTS) 1.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCTSV100 = ciscoSyslogCapCTSV100.setStatus('current')
ciscoSyslogCapCTMV1000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCTMV1000 = ciscoSyslogCapCTMV1000.setProductRelease('Cisco TelePresence Manager (CTM) 1.0.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapCTMV1000 = ciscoSyslogCapCTMV1000.setStatus('current')
ciscoSyslogCapc4710aceVA1R70 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapc4710aceVA1R70 = ciscoSyslogCapc4710aceVA1R70.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapc4710aceVA1R70 = ciscoSyslogCapc4710aceVA1R70.setStatus('current')
ciscoSyslogCapVqe = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 61, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapVqe = ciscoSyslogCapVqe.setProductRelease('VQE 3.5 release.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSyslogCapVqe = ciscoSyslogCapVqe.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYSLOG-CAPABILITY", ciscoSyslogCapCTSV100=ciscoSyslogCapCTSV100, ciscoSyslogCapability=ciscoSyslogCapability, ciscoSyslogCapACSWV03R000=ciscoSyslogCapACSWV03R000, PYSNMP_MODULE_ID=ciscoSyslogCapability, ciscoSyslogCapCTMV1000=ciscoSyslogCapCTMV1000, ciscoSyslogCapc4710aceVA1R70=ciscoSyslogCapc4710aceVA1R70, ciscoSyslogCapCatOSV08R0101=ciscoSyslogCapCatOSV08R0101, ciscoSyslogCapVqe=ciscoSyslogCapVqe)
