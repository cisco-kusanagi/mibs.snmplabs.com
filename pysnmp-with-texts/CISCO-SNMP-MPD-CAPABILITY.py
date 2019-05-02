#
# PySNMP MIB module CISCO-SNMP-MPD-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SNMP-MPD-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:12:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
TimeTicks, NotificationType, iso, Gauge32, IpAddress, Integer32, Counter64, ModuleIdentity, Bits, Unsigned32, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "iso", "Gauge32", "IpAddress", "Integer32", "Counter64", "ModuleIdentity", "Bits", "Unsigned32", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSnmpMpdCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 317))
ciscoSnmpMpdCapability.setRevisions(('2008-02-11 00:00', '2006-05-27 00:00', '2004-01-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpMpdCapability.setRevisionsDescriptions(('Added capability statement cSnmpMpdCapabilityc4710aceVA1R700 for ACE 4710 Application Control Engine Appliance.', 'Added capability statement cSnmpMpdCapabilityACSWV03R000 for Application Control Engine (ACE).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpMpdCapability.setLastUpdated('200802110000Z')
if mibBuilder.loadTexts: ciscoSnmpMpdCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpMpdCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com, cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpMpdCapability.setDescription('The capabilities description of SNMP-MPD-MIB.')
cSnmpMpdCapabilityCatOSV05R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 317, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpMpdCapabilityCatOSV05R0401 = cSnmpMpdCapabilityCatOSV05R0401.setProductRelease('Cisco CatOS 5.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpMpdCapabilityCatOSV05R0401 = cSnmpMpdCapabilityCatOSV05R0401.setStatus('current')
if mibBuilder.loadTexts: cSnmpMpdCapabilityCatOSV05R0401.setDescription('SNMP-MPD-MIB capabilities.')
cSnmpMpdCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 317, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpMpdCapabilityACSWV03R000 = cSnmpMpdCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpMpdCapabilityACSWV03R000 = cSnmpMpdCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: cSnmpMpdCapabilityACSWV03R000.setDescription('SNMP-MPD-MIB capabilities.')
cSnmpMpdCapabilityc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 317, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpMpdCapabilityc4710aceVA1R700 = cSnmpMpdCapabilityc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                     for ACE 4710 Application Control Engine \n                     Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpMpdCapabilityc4710aceVA1R700 = cSnmpMpdCapabilityc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: cSnmpMpdCapabilityc4710aceVA1R700.setDescription('SNMP-MPD-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SNMP-MPD-CAPABILITY", cSnmpMpdCapabilityACSWV03R000=cSnmpMpdCapabilityACSWV03R000, cSnmpMpdCapabilityCatOSV05R0401=cSnmpMpdCapabilityCatOSV05R0401, cSnmpMpdCapabilityc4710aceVA1R700=cSnmpMpdCapabilityc4710aceVA1R700, ciscoSnmpMpdCapability=ciscoSnmpMpdCapability, PYSNMP_MODULE_ID=ciscoSnmpMpdCapability)
