#
# PySNMP MIB module CISCO-LICENSE-MGR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-LICENSE-MGR-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:47:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Integer32, ObjectIdentity, NotificationType, iso, IpAddress, Counter32, Bits, Unsigned32, Counter64, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "NotificationType", "iso", "IpAddress", "Counter32", "Bits", "Unsigned32", "Counter64", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoLicenseMgrCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 495))
ciscoLicenseMgrCapability.setRevisions(('2008-07-21 00:00', '2006-03-08 00:00',))
if mibBuilder.loadTexts: ciscoLicenseMgrCapability.setLastUpdated('200807210000Z')
if mibBuilder.loadTexts: ciscoLicenseMgrCapability.setOrganization('Cisco Systems, Inc.')
ciscoLicenseMgrCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 495, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLicenseMgrCapabilityACSWV03R000 = ciscoLicenseMgrCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLicenseMgrCapabilityACSWV03R000 = ciscoLicenseMgrCapabilityACSWV03R000.setStatus('current')
ciscoLicMgrCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 495, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLicMgrCapc4710aceVA1R700 = ciscoLicMgrCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                 for ACE 4710 Application Control Engine \n                 Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLicMgrCapc4710aceVA1R700 = ciscoLicMgrCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-LICENSE-MGR-CAPABILITY", ciscoLicMgrCapc4710aceVA1R700=ciscoLicMgrCapc4710aceVA1R700, ciscoLicenseMgrCapabilityACSWV03R000=ciscoLicenseMgrCapabilityACSWV03R000, ciscoLicenseMgrCapability=ciscoLicenseMgrCapability, PYSNMP_MODULE_ID=ciscoLicenseMgrCapability)
