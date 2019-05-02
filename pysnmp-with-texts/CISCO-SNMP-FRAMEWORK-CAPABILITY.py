#
# PySNMP MIB module CISCO-SNMP-FRAMEWORK-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SNMP-FRAMEWORK-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:12:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter32, ModuleIdentity, Unsigned32, Bits, Gauge32, IpAddress, Integer32, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Unsigned32", "Bits", "Gauge32", "IpAddress", "Integer32", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "ObjectIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSnmpFrameworkCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 315))
ciscoSnmpFrameworkCapability.setRevisions(('2007-11-12 00:00', '2006-05-27 00:00', '2003-09-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpFrameworkCapability.setRevisionsDescriptions(('Added capability statement cSnmpFrameworkCapc4710aceVA1R700 for ACE 4710 Application Control Engine Appliance.', 'Added capability statement cSnmpFrameworkCapACSWV03R000 for Application Control Engine (ACE).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpFrameworkCapability.setLastUpdated('200711120000Z')
if mibBuilder.loadTexts: ciscoSnmpFrameworkCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpFrameworkCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com, cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpFrameworkCapability.setDescription('The capabilities description of SNMP-FRAMEWORK-MIB.')
cSnmpFrameworkCapCatOSV05R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 315, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapCatOSV05R0401 = cSnmpFrameworkCapCatOSV05R0401.setProductRelease('Cisco CatOS 5.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapCatOSV05R0401 = cSnmpFrameworkCapCatOSV05R0401.setStatus('current')
if mibBuilder.loadTexts: cSnmpFrameworkCapCatOSV05R0401.setDescription('SNMP-FRAMEWORK-MIB capabilities.')
cSnmpFrameworkCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 315, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapACSWV03R000 = cSnmpFrameworkCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n                          for Application Control Engine (ACE) \n                          Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapACSWV03R000 = cSnmpFrameworkCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: cSnmpFrameworkCapACSWV03R000.setDescription('SNMP-FRAMEWORK-MIB capabilities.')
cSnmpFrameworkCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 315, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapc4710aceVA1R700 = cSnmpFrameworkCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                         for ACE 4710 Application Control Engine \n                         Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapc4710aceVA1R700 = cSnmpFrameworkCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: cSnmpFrameworkCapc4710aceVA1R700.setDescription('SNMP-FRAMEWORK-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SNMP-FRAMEWORK-CAPABILITY", ciscoSnmpFrameworkCapability=ciscoSnmpFrameworkCapability, cSnmpFrameworkCapc4710aceVA1R700=cSnmpFrameworkCapc4710aceVA1R700, cSnmpFrameworkCapCatOSV05R0401=cSnmpFrameworkCapCatOSV05R0401, cSnmpFrameworkCapACSWV03R000=cSnmpFrameworkCapACSWV03R000, PYSNMP_MODULE_ID=ciscoSnmpFrameworkCapability)
