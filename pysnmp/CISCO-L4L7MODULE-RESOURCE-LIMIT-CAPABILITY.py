#
# PySNMP MIB module CISCO-L4L7MODULE-RESOURCE-LIMIT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-L4L7MODULE-RESOURCE-LIMIT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:47:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
IpAddress, Unsigned32, MibIdentifier, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, ObjectIdentity, iso, NotificationType, Gauge32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "MibIdentifier", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "ObjectIdentity", "iso", "NotificationType", "Gauge32", "ModuleIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoL4L7ModRsrcLimCap = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 499))
ciscoL4L7ModRsrcLimCap.setRevisions(('2008-07-22 00:00', '2008-07-21 00:00', '2006-04-19 00:00',))
if mibBuilder.loadTexts: ciscoL4L7ModRsrcLimCap.setLastUpdated('200807220000Z')
if mibBuilder.loadTexts: ciscoL4L7ModRsrcLimCap.setOrganization('Cisco Systems, Inc.')
cL4L7ModRsrcLimCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 499, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapACSWV03R000 = cL4L7ModRsrcLimCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapACSWV03R000 = cL4L7ModRsrcLimCapACSWV03R000.setStatus('current')
cL4L7ModRsrcLimCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 499, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapc4710aceVA1R700 = cL4L7ModRsrcLimCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                for ACE 4710 Application Control Engine \n                Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapc4710aceVA1R700 = cL4L7ModRsrcLimCapc4710aceVA1R700.setStatus('current')
cL4L7ModRsrcLimCapc4710aceVA3R10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 499, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapc4710aceVA3R10 = cL4L7ModRsrcLimCapc4710aceVA3R10.setProductRelease('ACSW (Application Control Software) A3(1.0)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapc4710aceVA3R10 = cL4L7ModRsrcLimCapc4710aceVA3R10.setStatus('current')
mibBuilder.exportSymbols("CISCO-L4L7MODULE-RESOURCE-LIMIT-CAPABILITY", ciscoL4L7ModRsrcLimCap=ciscoL4L7ModRsrcLimCap, PYSNMP_MODULE_ID=ciscoL4L7ModRsrcLimCap, cL4L7ModRsrcLimCapc4710aceVA3R10=cL4L7ModRsrcLimCapc4710aceVA3R10, cL4L7ModRsrcLimCapACSWV03R000=cL4L7ModRsrcLimCapACSWV03R000, cL4L7ModRsrcLimCapc4710aceVA1R700=cL4L7ModRsrcLimCapc4710aceVA1R700)
