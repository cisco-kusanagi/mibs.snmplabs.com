#
# PySNMP MIB module DLB-GENERIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLB-GENERIC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:32:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
dlbMgmt, = mibBuilder.importSymbols("DELIBERANT-MIB", "dlbMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysLocation, = mibBuilder.importSymbols("SNMPv2-MIB", "sysLocation")
Counter32, NotificationType, ModuleIdentity, iso, Bits, Gauge32, TimeTicks, Integer32, ObjectIdentity, Counter64, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "ModuleIdentity", "iso", "Bits", "Gauge32", "TimeTicks", "Integer32", "ObjectIdentity", "Counter64", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlbGenericMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 32761, 3, 1))
dlbGenericMIB.setRevisions(('2009-02-13 00:00',))
if mibBuilder.loadTexts: dlbGenericMIB.setLastUpdated('200902130000Z')
if mibBuilder.loadTexts: dlbGenericMIB.setOrganization('Deliberant')
dlbGenericMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1))
dlbGenericNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0))
dlbGenericInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 1))
dlbPowerLoss = NotificationType((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0, 1)).setObjects(("SNMPv2-MIB", "sysLocation"))
if mibBuilder.loadTexts: dlbPowerLoss.setStatus('current')
dlbAdministrativeReboot = NotificationType((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0, 2)).setObjects(("SNMPv2-MIB", "sysLocation"))
if mibBuilder.loadTexts: dlbAdministrativeReboot.setStatus('current')
mibBuilder.exportSymbols("DLB-GENERIC-MIB", dlbGenericInfo=dlbGenericInfo, dlbPowerLoss=dlbPowerLoss, dlbGenericMIBObjects=dlbGenericMIBObjects, PYSNMP_MODULE_ID=dlbGenericMIB, dlbGenericNotifs=dlbGenericNotifs, dlbAdministrativeReboot=dlbAdministrativeReboot, dlbGenericMIB=dlbGenericMIB)
