#
# PySNMP MIB module CISCO-SNMP-VACM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SNMP-VACM-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:12:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
TimeTicks, Bits, ObjectIdentity, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, Integer32, Counter64, ModuleIdentity, MibIdentifier, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "ObjectIdentity", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "Integer32", "Counter64", "ModuleIdentity", "MibIdentifier", "Counter32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSnmpVacmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 333))
ciscoSnmpVacmCapability.setRevisions(('2008-08-04 00:00', '2007-06-22 00:00', '2006-05-22 00:00', '2003-09-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpVacmCapability.setRevisionsDescriptions(('Added capability statement ciscoSnmpVacmCapc4710aceVA1R700 for ACE 4710 Application Control Engine Appliance.', 'Added the correct mib name under the SUPPORTS clause for ciscoSnmpVacmCapCatOSV05R0501 and ciscoSnmpVacmCapACSWV03R000.', 'Added capability statement ciscoSnmpVacmCapACSWV03R000 for Application Control Engine (ACE).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpVacmCapability.setLastUpdated('200808040000Z')
if mibBuilder.loadTexts: ciscoSnmpVacmCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpVacmCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com, cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpVacmCapability.setDescription('The capabilities description of SNMP-VIEW-BASED-ACM-MIB.')
ciscoSnmpVacmCapCatOSV05R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 333, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapCatOSV05R0501 = ciscoSnmpVacmCapCatOSV05R0501.setProductRelease('Cisco CatOS 5.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapCatOSV05R0501 = ciscoSnmpVacmCapCatOSV05R0501.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpVacmCapCatOSV05R0501.setDescription('SNMP-VIEW-BASED-ACM-MIB capabilities.')
ciscoSnmpVacmCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 333, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapACSWV03R000 = ciscoSnmpVacmCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapACSWV03R000 = ciscoSnmpVacmCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpVacmCapACSWV03R000.setDescription('SNMP-VIEW-BASED-ACM-MIB capabilities.')
ciscoSnmpVacmCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 333, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapc4710aceVA1R700 = ciscoSnmpVacmCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                         for ACE 4710 Application Control Engine \n                         Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpVacmCapc4710aceVA1R700 = ciscoSnmpVacmCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpVacmCapc4710aceVA1R700.setDescription('SNMP-VIEW-BASED-ACM-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SNMP-VACM-CAPABILITY", ciscoSnmpVacmCapability=ciscoSnmpVacmCapability, ciscoSnmpVacmCapACSWV03R000=ciscoSnmpVacmCapACSWV03R000, ciscoSnmpVacmCapCatOSV05R0501=ciscoSnmpVacmCapCatOSV05R0501, ciscoSnmpVacmCapc4710aceVA1R700=ciscoSnmpVacmCapc4710aceVA1R700, PYSNMP_MODULE_ID=ciscoSnmpVacmCapability)
