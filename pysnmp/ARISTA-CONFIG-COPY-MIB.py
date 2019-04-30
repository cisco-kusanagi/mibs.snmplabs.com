#
# PySNMP MIB module ARISTA-CONFIG-COPY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-CONFIG-COPY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:09:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaProducts, aristaModules, aristaMibs = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaProducts", "aristaModules", "aristaMibs")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, NotificationType, Unsigned32, IpAddress, MibIdentifier, Bits, TimeTicks, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "NotificationType", "Unsigned32", "IpAddress", "MibIdentifier", "Bits", "TimeTicks", "iso", "ObjectIdentity")
TextualConvention, RowStatus, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "DateAndTime")
aristaConfigCopyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 7))
aristaConfigCopyMIB.setRevisions(('2014-08-15 00:00', '2013-02-14 00:00',))
if mibBuilder.loadTexts: aristaConfigCopyMIB.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaConfigCopyMIB.setOrganization('Arista Networks, Inc.')
class ConfigCopyState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("inactive", 0), ("scheduled", 1), ("running", 2), ("completed", 3), ("failed", 4))

class ConfigCopyFailureCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("unknown", 1), ("timeout", 2))

aristaConfigCopyCommandTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1), )
if mibBuilder.loadTexts: aristaConfigCopyCommandTable.setStatus('current')
aristaConfigCopyCommandEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1), ).setIndexNames((0, "ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyName"), (0, "ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyId"))
if mibBuilder.loadTexts: aristaConfigCopyCommandEntry.setStatus('current')
aristaConfigCopyName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)))
if mibBuilder.loadTexts: aristaConfigCopyName.setStatus('current')
aristaConfigCopyId = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: aristaConfigCopyId.setStatus('current')
aristaConfigCopySourceUri = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aristaConfigCopySourceUri.setStatus('current')
aristaConfigCopyDestUri = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aristaConfigCopyDestUri.setStatus('current')
aristaConfigCopyState = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 5), ConfigCopyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaConfigCopyState.setStatus('current')
aristaConfigCopyTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 6), Unsigned32().clone(60)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aristaConfigCopyTimeout.setStatus('current')
aristaConfigCopyTimeStarted = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaConfigCopyTimeStarted.setStatus('current')
aristaConfigCopyTimeCompleted = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaConfigCopyTimeCompleted.setStatus('current')
aristaConfigCopyFailureCause = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 9), ConfigCopyFailureCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaConfigCopyFailureCause.setStatus('current')
aristaConfigCopyFailureMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaConfigCopyFailureMessage.setStatus('current')
aristaConfigCopyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 7, 1, 1, 11), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aristaConfigCopyRowStatus.setStatus('current')
aristaConfigCopyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 7, 2))
aristaConfigCopyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 7, 2, 1))
aristaConfigCopyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 7, 2, 2))
aristaConfigCopyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 7, 2, 1, 1)).setObjects(("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaConfigCopyCompliance = aristaConfigCopyCompliance.setStatus('current')
aristaConfigCopyObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 7, 2, 2, 1)).setObjects(("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopySourceUri"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyDestUri"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyState"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyTimeout"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyTimeStarted"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyTimeCompleted"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyFailureCause"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyFailureMessage"), ("ARISTA-CONFIG-COPY-MIB", "aristaConfigCopyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaConfigCopyObjectsGroup = aristaConfigCopyObjectsGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-CONFIG-COPY-MIB", aristaConfigCopySourceUri=aristaConfigCopySourceUri, aristaConfigCopyObjectsGroup=aristaConfigCopyObjectsGroup, aristaConfigCopyFailureMessage=aristaConfigCopyFailureMessage, ConfigCopyState=ConfigCopyState, aristaConfigCopyDestUri=aristaConfigCopyDestUri, aristaConfigCopyTimeStarted=aristaConfigCopyTimeStarted, aristaConfigCopyTimeCompleted=aristaConfigCopyTimeCompleted, aristaConfigCopyTimeout=aristaConfigCopyTimeout, aristaConfigCopyName=aristaConfigCopyName, aristaConfigCopyConformance=aristaConfigCopyConformance, PYSNMP_MODULE_ID=aristaConfigCopyMIB, aristaConfigCopyCommandTable=aristaConfigCopyCommandTable, aristaConfigCopyRowStatus=aristaConfigCopyRowStatus, aristaConfigCopyCompliance=aristaConfigCopyCompliance, aristaConfigCopyGroups=aristaConfigCopyGroups, aristaConfigCopyCompliances=aristaConfigCopyCompliances, aristaConfigCopyMIB=aristaConfigCopyMIB, aristaConfigCopyCommandEntry=aristaConfigCopyCommandEntry, aristaConfigCopyId=aristaConfigCopyId, ConfigCopyFailureCause=ConfigCopyFailureCause, aristaConfigCopyState=aristaConfigCopyState, aristaConfigCopyFailureCause=aristaConfigCopyFailureCause)
