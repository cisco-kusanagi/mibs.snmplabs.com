#
# PySNMP MIB module BW-BroadworksResourceAccess (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BW-BroadworksResourceAccess
# Produced by pysmi-0.3.4 at Wed May  1 11:42:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Unsigned32, IpAddress, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, iso, Counter32, enterprises, TimeTicks, Integer32, MibIdentifier, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "iso", "Counter32", "enterprises", "TimeTicks", "Integer32", "MibIdentifier", "Counter64", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
broadsoft = ModuleIdentity((1, 3, 6, 1, 4, 1, 6431))
if mibBuilder.loadTexts: broadsoft.setLastUpdated('200803011000Z')
if mibBuilder.loadTexts: broadsoft.setOrganization('Broadsoft, Inc')
if mibBuilder.loadTexts: broadsoft.setContactInfo('Broadsoft, Inc 220 Perry Parkway Gaithersburg, MD 20877 301-977-9440')
if mibBuilder.loadTexts: broadsoft.setDescription('The BW-BroadworksResourceAccess.mib is introduces to capture the performance measurements for the BroadWorks Resource Access.')
broadworks = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1))
resourceAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 13))
operations = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 13, 1))
bwResourceAccessMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 13, 1000))
bwFileGets = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 13, 1, 1), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwFileGets.setStatus('current')
if mibBuilder.loadTexts: bwFileGets.setDescription('This counter reflects the number of times the application gets a file from the file repository.')
bwFileDeletes = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 13, 1, 2), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwFileDeletes.setStatus('current')
if mibBuilder.loadTexts: bwFileDeletes.setDescription('This counter reflects the number of times the application deletes a file from the file repository.')
bwFilePuts = MibScalar((1, 3, 6, 1, 4, 1, 6431, 1, 13, 1, 3), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bwFilePuts.setStatus('current')
if mibBuilder.loadTexts: bwFilePuts.setDescription('This counter reflects the number of times the application saves a file in the file repository.')
bwResourceAccessMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 13, 1000, 1))
bwResourceAccessMibCompliancy = MibIdentifier((1, 3, 6, 1, 4, 1, 6431, 1, 13, 1000, 2))
bwResourceAccessOperationsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6431, 1, 13, 1000, 1, 1)).setObjects(("BW-BroadworksResourceAccess", "bwFileGets"), ("BW-BroadworksResourceAccess", "bwFileDeletes"), ("BW-BroadworksResourceAccess", "bwFilePuts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwResourceAccessOperationsGroup = bwResourceAccessOperationsGroup.setStatus('current')
if mibBuilder.loadTexts: bwResourceAccessOperationsGroup.setDescription('This group defines the operations statistics for the Resource Access component.')
bwResourceAccessBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6431, 1, 13, 1000, 2, 1)).setObjects(("BW-BroadworksResourceAccess", "bwResourceAccessOperationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bwResourceAccessBasicCompliance = bwResourceAccessBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: bwResourceAccessBasicCompliance.setDescription('BroadWorks Resource Access MIB compliance')
mibBuilder.exportSymbols("BW-BroadworksResourceAccess", broadworks=broadworks, resourceAccess=resourceAccess, operations=operations, bwResourceAccessMibGroups=bwResourceAccessMibGroups, PYSNMP_MODULE_ID=broadsoft, bwFilePuts=bwFilePuts, bwResourceAccessMibCompliancy=bwResourceAccessMibCompliancy, bwResourceAccessOperationsGroup=bwResourceAccessOperationsGroup, bwResourceAccessMibConformance=bwResourceAccessMibConformance, broadsoft=broadsoft, bwFileDeletes=bwFileDeletes, bwResourceAccessBasicCompliance=bwResourceAccessBasicCompliance, bwFileGets=bwFileGets)
