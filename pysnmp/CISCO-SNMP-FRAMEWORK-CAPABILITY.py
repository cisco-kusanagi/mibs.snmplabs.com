#
# PySNMP MIB module CISCO-SNMP-FRAMEWORK-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SNMP-FRAMEWORK-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:55:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Bits, ObjectIdentity, Integer32, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Gauge32, NotificationType, ModuleIdentity, Unsigned32, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "Integer32", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Gauge32", "NotificationType", "ModuleIdentity", "Unsigned32", "MibIdentifier", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSnmpFrameworkCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 315))
ciscoSnmpFrameworkCapability.setRevisions(('2007-11-12 00:00', '2006-05-27 00:00', '2003-09-03 00:00',))
if mibBuilder.loadTexts: ciscoSnmpFrameworkCapability.setLastUpdated('200711120000Z')
if mibBuilder.loadTexts: ciscoSnmpFrameworkCapability.setOrganization('Cisco Systems, Inc.')
cSnmpFrameworkCapCatOSV05R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 315, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapCatOSV05R0401 = cSnmpFrameworkCapCatOSV05R0401.setProductRelease('Cisco CatOS 5.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapCatOSV05R0401 = cSnmpFrameworkCapCatOSV05R0401.setStatus('current')
cSnmpFrameworkCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 315, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapACSWV03R000 = cSnmpFrameworkCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n                          for Application Control Engine (ACE) \n                          Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapACSWV03R000 = cSnmpFrameworkCapACSWV03R000.setStatus('current')
cSnmpFrameworkCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 315, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapc4710aceVA1R700 = cSnmpFrameworkCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                         for ACE 4710 Application Control Engine \n                         Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSnmpFrameworkCapc4710aceVA1R700 = cSnmpFrameworkCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMP-FRAMEWORK-CAPABILITY", ciscoSnmpFrameworkCapability=ciscoSnmpFrameworkCapability, cSnmpFrameworkCapc4710aceVA1R700=cSnmpFrameworkCapc4710aceVA1R700, PYSNMP_MODULE_ID=ciscoSnmpFrameworkCapability, cSnmpFrameworkCapCatOSV05R0401=cSnmpFrameworkCapCatOSV05R0401, cSnmpFrameworkCapACSWV03R000=cSnmpFrameworkCapACSWV03R000)
