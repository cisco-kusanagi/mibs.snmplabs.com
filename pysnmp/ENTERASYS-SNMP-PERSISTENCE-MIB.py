#
# PySNMP MIB module ENTERASYS-SNMP-PERSISTENCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-SNMP-PERSISTENCE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:50:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, IpAddress, Bits, Counter32, NotificationType, Unsigned32, TimeTicks, iso, ModuleIdentity, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "Bits", "Counter32", "NotificationType", "Unsigned32", "TimeTicks", "iso", "ModuleIdentity", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32")
TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "DateAndTime")
etsysSnmpPersistenceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24))
etsysSnmpPersistenceMIB.setRevisions(('2002-09-09 20:22',))
if mibBuilder.loadTexts: etsysSnmpPersistenceMIB.setLastUpdated('200209092022Z')
if mibBuilder.loadTexts: etsysSnmpPersistenceMIB.setOrganization('Enterasys Networks Inc')
etsysSnmpPersistenceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1))
etsysSnmpPersistenceMode = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("snmpNormalSave", 1), ("pushButtonSave", 2), ("timeDelayedSave", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSnmpPersistenceMode.setStatus('current')
etsysSnmpPersistenceSave = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nop", 1), ("save", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSnmpPersistenceSave.setStatus('current')
etsysSnmpPersistenceStatus = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("unsavedChanges", 2), ("savingChanges", 3), ("saveSucceeded", 4), ("saveFailed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSnmpPersistenceStatus.setStatus('current')
etsysSnmpPersistenceStatusTime = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSnmpPersistenceStatusTime.setStatus('current')
etsysSnmpPersistenceError = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSnmpPersistenceError.setStatus('current')
etsysSnmpPersistenceErrorTime = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSnmpPersistenceErrorTime.setStatus('current')
etsysSnmpPersistenceConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 2))
etsysSnmpPersistenceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 2, 1))
etsysSnmpPersistenceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 2, 2))
etsysSnmpPersistenceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 2, 1, 1)).setObjects(("ENTERASYS-SNMP-PERSISTENCE-MIB", "etsysSnmpPersistenceMode"), ("ENTERASYS-SNMP-PERSISTENCE-MIB", "etsysSnmpPersistenceSave"), ("ENTERASYS-SNMP-PERSISTENCE-MIB", "etsysSnmpPersistenceStatus"), ("ENTERASYS-SNMP-PERSISTENCE-MIB", "etsysSnmpPersistenceStatusTime"), ("ENTERASYS-SNMP-PERSISTENCE-MIB", "etsysSnmpPersistenceError"), ("ENTERASYS-SNMP-PERSISTENCE-MIB", "etsysSnmpPersistenceErrorTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSnmpPersistenceGroup = etsysSnmpPersistenceGroup.setStatus('current')
etsysSnmpPersistenceCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 2, 2, 1)).setObjects(("ENTERASYS-SNMP-PERSISTENCE-MIB", "etsysSnmpPersistenceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSnmpPersistenceCompliance = etsysSnmpPersistenceCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-SNMP-PERSISTENCE-MIB", PYSNMP_MODULE_ID=etsysSnmpPersistenceMIB, etsysSnmpPersistenceStatusTime=etsysSnmpPersistenceStatusTime, etsysSnmpPersistenceCompliance=etsysSnmpPersistenceCompliance, etsysSnmpPersistenceErrorTime=etsysSnmpPersistenceErrorTime, etsysSnmpPersistenceSave=etsysSnmpPersistenceSave, etsysSnmpPersistenceGroups=etsysSnmpPersistenceGroups, etsysSnmpPersistenceMIB=etsysSnmpPersistenceMIB, etsysSnmpPersistenceCompliances=etsysSnmpPersistenceCompliances, etsysSnmpPersistenceError=etsysSnmpPersistenceError, etsysSnmpPersistenceMode=etsysSnmpPersistenceMode, etsysSnmpPersistenceObjects=etsysSnmpPersistenceObjects, etsysSnmpPersistenceStatus=etsysSnmpPersistenceStatus, etsysSnmpPersistenceConformance=etsysSnmpPersistenceConformance, etsysSnmpPersistenceGroup=etsysSnmpPersistenceGroup)
