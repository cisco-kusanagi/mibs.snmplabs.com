#
# PySNMP MIB module CISCO-DSP-MGMT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-DSP-MGMT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:38:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Bits, iso, TimeTicks, Gauge32, Unsigned32, Counter64, NotificationType, ObjectIdentity, IpAddress, Integer32, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "TimeTicks", "Gauge32", "Unsigned32", "Counter64", "NotificationType", "ObjectIdentity", "IpAddress", "Integer32", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoDspMgmtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 121))
ciscoDspMgmtCapability.setRevisions(('2011-04-18 00:00', '2006-08-09 00:00', '2005-10-16 00:00', '2005-06-29 00:00', '2005-04-21 00:00', '2004-08-07 00:00', '2003-09-18 00:00',))
if mibBuilder.loadTexts: ciscoDspMgmtCapability.setLastUpdated('201104180000Z')
if mibBuilder.loadTexts: ciscoDspMgmtCapability.setOrganization('Cisco Systems, Inc.')
ciscoDspMgmtCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R00 = ciscoDspMgmtCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R00 = ciscoDspMgmtCapabilityV5R00.setStatus('current')
ciscoDspMgmtCapabilityV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R015 = ciscoDspMgmtCapabilityV5R015.setProductRelease('MGX8850 Release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R015 = ciscoDspMgmtCapabilityV5R015.setStatus('current')
ciscoDspMgmtCapabilityV5R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R100 = ciscoDspMgmtCapabilityV5R100.setProductRelease('MGX8880 Release 5.1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R100 = ciscoDspMgmtCapabilityV5R100.setStatus('current')
ciscoDspMgmtCapabilityV12R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV12R03 = ciscoDspMgmtCapabilityV12R03.setProductRelease('Cisco IOS 12.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV12R03 = ciscoDspMgmtCapabilityV12R03.setStatus('current')
ciscoDspMgmtCapabilityV5R300 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R300 = ciscoDspMgmtCapabilityV5R300.setProductRelease('MGX8880 Release 5.3.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R300 = ciscoDspMgmtCapabilityV5R300.setStatus('current')
ciscoDspMgmtCapabilityV5R400 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R400 = ciscoDspMgmtCapabilityV5R400.setProductRelease('MGX8880 Release 5.4.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV5R400 = ciscoDspMgmtCapabilityV5R400.setStatus('current')
ciscoDspMgmtCapabilityV15R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 121, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV15R02 = ciscoDspMgmtCapabilityV15R02.setProductRelease('OS=IOS\n                     OSVERSION=15.2(1)T\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDspMgmtCapabilityV15R02 = ciscoDspMgmtCapabilityV15R02.setStatus('current')
mibBuilder.exportSymbols("CISCO-DSP-MGMT-CAPABILITY", PYSNMP_MODULE_ID=ciscoDspMgmtCapability, ciscoDspMgmtCapabilityV15R02=ciscoDspMgmtCapabilityV15R02, ciscoDspMgmtCapabilityV5R015=ciscoDspMgmtCapabilityV5R015, ciscoDspMgmtCapabilityV5R00=ciscoDspMgmtCapabilityV5R00, ciscoDspMgmtCapabilityV5R300=ciscoDspMgmtCapabilityV5R300, ciscoDspMgmtCapabilityV12R03=ciscoDspMgmtCapabilityV12R03, ciscoDspMgmtCapabilityV5R400=ciscoDspMgmtCapabilityV5R400, ciscoDspMgmtCapabilityV5R100=ciscoDspMgmtCapabilityV5R100, ciscoDspMgmtCapability=ciscoDspMgmtCapability)
