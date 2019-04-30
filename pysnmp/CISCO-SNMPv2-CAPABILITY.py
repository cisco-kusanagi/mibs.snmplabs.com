#
# PySNMP MIB module CISCO-SNMPv2-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SNMPv2-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:55:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter32, TimeTicks, ModuleIdentity, NotificationType, Integer32, MibIdentifier, IpAddress, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "ModuleIdentity", "NotificationType", "Integer32", "MibIdentifier", "IpAddress", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "Bits", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSnmpV2Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 113))
ciscoSnmpV2Capability.setRevisions(('2007-11-12 00:00', '2006-05-30 00:00', '2006-04-24 00:00', '2004-03-18 00:00', '2002-02-07 00:00', '2002-01-31 00:00', '1994-08-18 00:00',))
if mibBuilder.loadTexts: ciscoSnmpV2Capability.setLastUpdated('200711120000Z')
if mibBuilder.loadTexts: ciscoSnmpV2Capability.setOrganization('Cisco Systems, Inc.')
ciscoSnmpV2CapabilityV10R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapabilityV10R02 = ciscoSnmpV2CapabilityV10R02.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapabilityV10R02 = ciscoSnmpV2CapabilityV10R02.setStatus('current')
ciscoRpmsSnmpV2CapabilityV20 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRpmsSnmpV2CapabilityV20 = ciscoRpmsSnmpV2CapabilityV20.setProductRelease('Cisco Resource Policy Management Server (RPMS) 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRpmsSnmpV2CapabilityV20 = ciscoRpmsSnmpV2CapabilityV20.setStatus('current')
ciscoMgxSnmpV2CapabilityV20 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMgxSnmpV2CapabilityV20 = ciscoMgxSnmpV2CapabilityV20.setProductRelease('MGX8850 Release 2.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMgxSnmpV2CapabilityV20 = ciscoMgxSnmpV2CapabilityV20.setStatus('current')
ciscoBpxSesSnmpV2CapabilityV10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBpxSesSnmpV2CapabilityV10 = ciscoBpxSesSnmpV2CapabilityV10.setProductRelease('Cisco BPX SES Release 1.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoBpxSesSnmpV2CapabilityV10 = ciscoBpxSesSnmpV2CapabilityV10.setStatus('current')
ciscoSnmpV2CapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapCatOSV08R0301 = ciscoSnmpV2CapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) for Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapCatOSV08R0301 = ciscoSnmpV2CapCatOSV08R0301.setStatus('current')
ciscoSnmpV2CapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapCatOSV08R0601 = ciscoSnmpV2CapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1) for Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapCatOSV08R0601 = ciscoSnmpV2CapCatOSV08R0601.setStatus('current')
ciscoSnmpV2CapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapACSWV03R000 = ciscoSnmpV2CapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0\n                          for Application Control Engine (ACE) \n                          Service Module.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2CapACSWV03R000 = ciscoSnmpV2CapACSWV03R000.setStatus('current')
ciscoSnmpV2Capc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 113, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2Capc4710aceVA1R700 = ciscoSnmpV2Capc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSnmpV2Capc4710aceVA1R700 = ciscoSnmpV2Capc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-SNMPv2-CAPABILITY", ciscoSnmpV2Capability=ciscoSnmpV2Capability, ciscoSnmpV2CapACSWV03R000=ciscoSnmpV2CapACSWV03R000, PYSNMP_MODULE_ID=ciscoSnmpV2Capability, ciscoMgxSnmpV2CapabilityV20=ciscoMgxSnmpV2CapabilityV20, ciscoSnmpV2CapabilityV10R02=ciscoSnmpV2CapabilityV10R02, ciscoBpxSesSnmpV2CapabilityV10=ciscoBpxSesSnmpV2CapabilityV10, ciscoSnmpV2CapCatOSV08R0601=ciscoSnmpV2CapCatOSV08R0601, ciscoRpmsSnmpV2CapabilityV20=ciscoRpmsSnmpV2CapabilityV20, ciscoSnmpV2Capc4710aceVA1R700=ciscoSnmpV2Capc4710aceVA1R700, ciscoSnmpV2CapCatOSV08R0301=ciscoSnmpV2CapCatOSV08R0301)
