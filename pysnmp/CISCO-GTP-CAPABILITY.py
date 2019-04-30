#
# PySNMP MIB module CISCO-GTP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-GTP-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:42:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibIdentifier, Counter32, Counter64, iso, ModuleIdentity, ObjectIdentity, Gauge32, NotificationType, TimeTicks, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "Counter32", "Counter64", "iso", "ModuleIdentity", "ObjectIdentity", "Gauge32", "NotificationType", "TimeTicks", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGtpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 263))
ciscoGtpCapability.setRevisions(('2003-04-02 09:00', '2002-03-21 16:00',))
if mibBuilder.loadTexts: ciscoGtpCapability.setLastUpdated('200304020900Z')
if mibBuilder.loadTexts: ciscoGtpCapability.setOrganization('Cisco Systems, Inc.')
cGtpCapabilityV12R02Rev08YD = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 263, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YD = cGtpCapabilityV12R02Rev08YD.setProductRelease('Cisco IOS 12.2(8)YD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YD = cGtpCapabilityV12R02Rev08YD.setStatus('current')
cGtpCapabilityV12R02Rev08YY = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 263, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YY = cGtpCapabilityV12R02Rev08YY.setProductRelease('Cisco IOS 12.2(8)YY')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YY = cGtpCapabilityV12R02Rev08YY.setStatus('current')
cGtpCapabilityV12R02Rev08YW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 263, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YW = cGtpCapabilityV12R02Rev08YW.setProductRelease('Cisco IOS 12.2(8)YW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cGtpCapabilityV12R02Rev08YW = cGtpCapabilityV12R02Rev08YW.setStatus('current')
mibBuilder.exportSymbols("CISCO-GTP-CAPABILITY", cGtpCapabilityV12R02Rev08YY=cGtpCapabilityV12R02Rev08YY, PYSNMP_MODULE_ID=ciscoGtpCapability, cGtpCapabilityV12R02Rev08YD=cGtpCapabilityV12R02Rev08YD, ciscoGtpCapability=ciscoGtpCapability, cGtpCapabilityV12R02Rev08YW=cGtpCapabilityV12R02Rev08YW)
