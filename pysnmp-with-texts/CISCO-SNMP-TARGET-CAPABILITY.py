#
# PySNMP MIB module CISCO-SNMP-TARGET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SNMP-TARGET-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:12:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
NotificationType, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Integer32, IpAddress, Counter64, Counter32, Gauge32, TimeTicks, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Integer32", "IpAddress", "Counter64", "Counter32", "Gauge32", "TimeTicks", "MibIdentifier", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSnmpTargetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 359))
ciscoSnmpTargetCapability.setRevisions(('2008-07-21 00:00', '2007-06-22 00:00', '2006-04-11 00:00', '2004-07-28 00:00', '2003-09-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpTargetCapability.setRevisionsDescriptions(('Added capability statement ciscoSnmpTargetCapc4710aceVA1R700 for ACE 4710 Application Control Engine Appliance. Added VARIATION clause for snmpTargetSpinLock object in ciscoSnmpTargetCapACSWV03R000 agent capability.', 'Removed SYNTAX for snmpTargetAddrTDomain under ciscoSnmpTargetCapCatOSV05R0501.', 'Added capability statement ciscoSnmpTargetCapACSWV03R000 for Application Control Engine (ACE).', 'Added capabilities for VISM release 3.3.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpTargetCapability.setLastUpdated('200807210000Z')
if mibBuilder.loadTexts: ciscoSnmpTargetCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpTargetCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com, cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpTargetCapability.setDescription('The capabilities description of SNMP-TARGET-MIB.')
ciscoSnmpTargetCapCatOSV05R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 359, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapCatOSV05R0501 = ciscoSnmpTargetCapCatOSV05R0501.setProductRelease('Cisco CatOS 5.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapCatOSV05R0501 = ciscoSnmpTargetCapCatOSV05R0501.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpTargetCapCatOSV05R0501.setDescription('SNMP-TARGET-MIB capabilities.')
ciscoSnmpTargetCapVISM33 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 359, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapVISM33 = ciscoSnmpTargetCapVISM33.setProductRelease('Cisco VISM Release 3.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapVISM33 = ciscoSnmpTargetCapVISM33.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpTargetCapVISM33.setDescription('SNMP-TARGET-MIB capabilities.')
ciscoSnmpTargetCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 359, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapACSWV03R000 = ciscoSnmpTargetCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapACSWV03R000 = ciscoSnmpTargetCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpTargetCapACSWV03R000.setDescription('SNMP-TARGET-MIB capabilities.')
ciscoSnmpTargetCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 359, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapc4710aceVA1R700 = ciscoSnmpTargetCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                     for ACE 4710 Application Control Engine \n                     Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpTargetCapc4710aceVA1R700 = ciscoSnmpTargetCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpTargetCapc4710aceVA1R700.setDescription('SNMP-TARGET-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SNMP-TARGET-CAPABILITY", ciscoSnmpTargetCapability=ciscoSnmpTargetCapability, PYSNMP_MODULE_ID=ciscoSnmpTargetCapability, ciscoSnmpTargetCapc4710aceVA1R700=ciscoSnmpTargetCapc4710aceVA1R700, ciscoSnmpTargetCapCatOSV05R0501=ciscoSnmpTargetCapCatOSV05R0501, ciscoSnmpTargetCapVISM33=ciscoSnmpTargetCapVISM33, ciscoSnmpTargetCapACSWV03R000=ciscoSnmpTargetCapACSWV03R000)
