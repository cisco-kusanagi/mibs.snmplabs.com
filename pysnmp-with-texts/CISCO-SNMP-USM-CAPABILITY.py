#
# PySNMP MIB module CISCO-SNMP-USM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SNMP-USM-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:12:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Counter32, Unsigned32, NotificationType, MibIdentifier, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, ModuleIdentity, Bits, ObjectIdentity, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "NotificationType", "MibIdentifier", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "ModuleIdentity", "Bits", "ObjectIdentity", "IpAddress", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSnmpUsmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 323))
ciscoSnmpUsmCapability.setRevisions(('2008-08-01 00:00', '2006-05-22 00:00', '2003-08-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSnmpUsmCapability.setRevisionsDescriptions(('Added the correct mib name under the SUPPORTS clause for ciscoSnmpUsmCapCatOSV05R0501 and ciscoSnmpUsmCapACSWV03R000. Added terminating quotes for ciscoSnmpUsmCapACSWV03R000 PRODUCT-RELEASE clause. Added capability statement ciscoSnmpUsmCapc4710aceVA1R700 for ACE 4710 Application Control Engine Appliance.', 'Added capability statement ciscoSnmpUsmCapACSWV03R000 for Application Control Engine (ACE).', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSnmpUsmCapability.setLastUpdated('200808010000Z')
if mibBuilder.loadTexts: ciscoSnmpUsmCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSnmpUsmCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-lan-switch-snmp@cisco.com, cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSnmpUsmCapability.setDescription('The capabilities description of SNMP-USER-BASED-SM-MIB.')
ciscoSnmpUsmCapCatOSV05R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 323, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapCatOSV05R0501 = ciscoSnmpUsmCapCatOSV05R0501.setProductRelease('Cisco CatOS 5.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapCatOSV05R0501 = ciscoSnmpUsmCapCatOSV05R0501.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpUsmCapCatOSV05R0501.setDescription('SNMP-USER-BASED-SM-MIB capabilities.')
ciscoSnmpUsmCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 323, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapACSWV03R000 = ciscoSnmpUsmCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapACSWV03R000 = ciscoSnmpUsmCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpUsmCapACSWV03R000.setDescription('SNMP-USER-BASED-SM-MIB capabilities.')
ciscoSnmpUsmCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 323, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapc4710aceVA1R700 = ciscoSnmpUsmCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpUsmCapc4710aceVA1R700 = ciscoSnmpUsmCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoSnmpUsmCapc4710aceVA1R700.setDescription('SNMP-USER-BASED-SM-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SNMP-USM-CAPABILITY", PYSNMP_MODULE_ID=ciscoSnmpUsmCapability, ciscoSnmpUsmCapACSWV03R000=ciscoSnmpUsmCapACSWV03R000, ciscoSnmpUsmCapc4710aceVA1R700=ciscoSnmpUsmCapc4710aceVA1R700, ciscoSnmpUsmCapability=ciscoSnmpUsmCapability, ciscoSnmpUsmCapCatOSV05R0501=ciscoSnmpUsmCapCatOSV05R0501)
