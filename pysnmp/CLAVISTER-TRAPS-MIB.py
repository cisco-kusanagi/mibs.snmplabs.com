#
# PySNMP MIB module CLAVISTER-TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CLAVISTER-TRAPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:09:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
clavisterOSTrapInfo, clavisterOSTrap = mibBuilder.importSymbols("CLAVISTER-SMI", "clavisterOSTrapInfo", "clavisterOSTrap")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter64, Gauge32, IpAddress, TimeTicks, Bits, MibIdentifier, Integer32, ModuleIdentity, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "IpAddress", "TimeTicks", "Bits", "MibIdentifier", "Integer32", "ModuleIdentity", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
clavisterOSTrapMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 5089, 1, 1, 0))
clavisterOSTrapMibModule.setRevisions(('2006-05-19 09:00',))
if mibBuilder.loadTexts: clavisterOSTrapMibModule.setLastUpdated('200605190900Z')
if mibBuilder.loadTexts: clavisterOSTrapMibModule.setOrganization('Clavister AB')
clavisterOSTrapVarSeverity = MibScalar((1, 3, 6, 1, 4, 1, 5089, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clavisterOSTrapVarSeverity.setStatus('current')
clavisterOSTrapVarCategory = MibScalar((1, 3, 6, 1, 4, 1, 5089, 1, 1, 5), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clavisterOSTrapVarCategory.setStatus('current')
clavisterOSTrapVarID = MibScalar((1, 3, 6, 1, 4, 1, 5089, 1, 1, 6), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clavisterOSTrapVarID.setStatus('current')
clavisterOSTrapVarEvent = MibScalar((1, 3, 6, 1, 4, 1, 5089, 1, 1, 7), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clavisterOSTrapVarEvent.setStatus('current')
clavisterOSTrapVarAction = MibScalar((1, 3, 6, 1, 4, 1, 5089, 1, 1, 8), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clavisterOSTrapVarAction.setStatus('current')
clavisterOSTrapVarTime = MibScalar((1, 3, 6, 1, 4, 1, 5089, 1, 1, 9), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clavisterOSTrapVarTime.setStatus('current')
clavisterOSTrapVarMessage = MibScalar((1, 3, 6, 1, 4, 1, 5089, 1, 1, 10), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clavisterOSTrapVarMessage.setStatus('current')
clavisterOSGenericTrap = NotificationType((1, 3, 6, 1, 4, 1, 5089, 1, 0, 1)).setObjects(("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarSeverity"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarCategory"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarID"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarEvent"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarAction"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarTime"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarMessage"))
if mibBuilder.loadTexts: clavisterOSGenericTrap.setStatus('current')
clavisterOSTrapGroupTrap = NotificationGroup((1, 3, 6, 1, 4, 1, 5089, 1, 1, 1)).setObjects(("CLAVISTER-TRAPS-MIB", "clavisterOSGenericTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clavisterOSTrapGroupTrap = clavisterOSTrapGroupTrap.setStatus('current')
clavisterOSTrapGroupVar = ObjectGroup((1, 3, 6, 1, 4, 1, 5089, 1, 1, 2)).setObjects(("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarSeverity"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarCategory"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarID"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarEvent"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarAction"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarTime"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarMessage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clavisterOSTrapGroupVar = clavisterOSTrapGroupVar.setStatus('current')
clavisterOSTrapCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5089, 1, 1, 3)).setObjects(("CLAVISTER-TRAPS-MIB", "clavisterOSTrapGroupTrap"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapGroupVar"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clavisterOSTrapCompliance = clavisterOSTrapCompliance.setStatus('current')
mibBuilder.exportSymbols("CLAVISTER-TRAPS-MIB", PYSNMP_MODULE_ID=clavisterOSTrapMibModule, clavisterOSTrapVarCategory=clavisterOSTrapVarCategory, clavisterOSTrapGroupTrap=clavisterOSTrapGroupTrap, clavisterOSTrapVarSeverity=clavisterOSTrapVarSeverity, clavisterOSTrapVarAction=clavisterOSTrapVarAction, clavisterOSTrapCompliance=clavisterOSTrapCompliance, clavisterOSTrapMibModule=clavisterOSTrapMibModule, clavisterOSGenericTrap=clavisterOSGenericTrap, clavisterOSTrapVarMessage=clavisterOSTrapVarMessage, clavisterOSTrapVarID=clavisterOSTrapVarID, clavisterOSTrapVarEvent=clavisterOSTrapVarEvent, clavisterOSTrapVarTime=clavisterOSTrapVarTime, clavisterOSTrapGroupVar=clavisterOSTrapGroupVar)
