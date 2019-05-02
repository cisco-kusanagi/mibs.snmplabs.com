#
# PySNMP MIB module DLB-GENERIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLB-GENERIC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:47:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
dlbMgmt, = mibBuilder.importSymbols("DELIBERANT-MIB", "dlbMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysLocation, = mibBuilder.importSymbols("SNMPv2-MIB", "sysLocation")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, ObjectIdentity, Bits, MibIdentifier, Unsigned32, Integer32, NotificationType, Counter32, IpAddress, Gauge32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "ObjectIdentity", "Bits", "MibIdentifier", "Unsigned32", "Integer32", "NotificationType", "Counter32", "IpAddress", "Gauge32", "ModuleIdentity", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlbGenericMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 32761, 3, 1))
dlbGenericMIB.setRevisions(('2009-02-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dlbGenericMIB.setRevisionsDescriptions(('First revision.',))
if mibBuilder.loadTexts: dlbGenericMIB.setLastUpdated('200902130000Z')
if mibBuilder.loadTexts: dlbGenericMIB.setOrganization('Deliberant')
if mibBuilder.loadTexts: dlbGenericMIB.setContactInfo(' Deliberant Customer Support E-mail: support@deliberant.com')
if mibBuilder.loadTexts: dlbGenericMIB.setDescription('The Deliberant Generic MIB.')
dlbGenericMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1))
dlbGenericNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0))
dlbGenericInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 1))
dlbPowerLoss = NotificationType((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0, 1)).setObjects(("SNMPv2-MIB", "sysLocation"))
if mibBuilder.loadTexts: dlbPowerLoss.setStatus('current')
if mibBuilder.loadTexts: dlbPowerLoss.setDescription('This notification is sent on device boot after power loss or device crash.')
dlbAdministrativeReboot = NotificationType((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0, 2)).setObjects(("SNMPv2-MIB", "sysLocation"))
if mibBuilder.loadTexts: dlbAdministrativeReboot.setStatus('current')
if mibBuilder.loadTexts: dlbAdministrativeReboot.setDescription('This notification is sent on device boot after administrator rebooted device.')
mibBuilder.exportSymbols("DLB-GENERIC-MIB", dlbGenericMIB=dlbGenericMIB, dlbGenericMIBObjects=dlbGenericMIBObjects, dlbPowerLoss=dlbPowerLoss, PYSNMP_MODULE_ID=dlbGenericMIB, dlbGenericNotifs=dlbGenericNotifs, dlbGenericInfo=dlbGenericInfo, dlbAdministrativeReboot=dlbAdministrativeReboot)
