#
# PySNMP MIB module BW-BroadworksResourceAccess (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BW-BroadworksResourceAccess
# Produced by pysmi-0.3.4 at Mon Apr 29 17:24:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, TimeTicks, ObjectIdentity, MibIdentifier, IpAddress, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, Gauge32, ModuleIdentity, iso, Bits, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "ObjectIdentity", "MibIdentifier", "IpAddress", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "Gauge32", "ModuleIdentity", "iso", "Bits", "NotificationType", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
broadsoft = ModuleIdentity((1, 3, 6, 1, 4, 1, 6431))
if mibBuilder.loadTexts: broadsoft.setLastUpdated('200803011000Z')
if mibBuilder.loadTexts: broadsoft.setOrganization('Broadsoft, Inc')
broadworks = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1))
resourceAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 13))
operations = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 13, 1))
bwResourceAccessMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 13, 1000))
bwFileGets = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 13, 1, 1), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwFileGets.setStatus('current')
bwFileDeletes = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 13, 1, 2), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwFileDeletes.setStatus('current')
bwFilePuts = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 13, 1, 3), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwFilePuts.setStatus('current')
bwResourceAccessMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 13, 1000, 1))
bwResourceAccessMibCompliancy = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 13, 1000, 2))
bwResourceAccessOperationsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6431, 1, 13, 1000, 1, 1)).setObjects(("BW-BroadworksResourceAccess", "bwFileGets"), ("BW-BroadworksResourceAccess", "bwFileDeletes"), ("BW-BroadworksResourceAccess", "bwFilePuts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwResourceAccessOperationsGroup = bwResourceAccessOperationsGroup.setStatus('current')
bwResourceAccessBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6431, 1, 13, 1000, 2, 1)).setObjects(("BW-BroadworksResourceAccess", "bwResourceAccessOperationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwResourceAccessBasicCompliance = bwResourceAccessBasicCompliance.setStatus('current')
mibBuilder.exportSymbols("BW-BroadworksResourceAccess", bwResourceAccessMibCompliancy=bwResourceAccessMibCompliancy, broadworks=broadworks, bwResourceAccessBasicCompliance=bwResourceAccessBasicCompliance, PYSNMP_MODULE_ID=broadsoft, resourceAccess=resourceAccess, bwFileDeletes=bwFileDeletes, operations=operations, bwFilePuts=bwFilePuts, bwResourceAccessMibConformance=bwResourceAccessMibConformance, bwResourceAccessOperationsGroup=bwResourceAccessOperationsGroup, bwResourceAccessMibGroups=bwResourceAccessMibGroups, broadsoft=broadsoft, bwFileGets=bwFileGets)
