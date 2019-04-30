#
# PySNMP MIB module ELTEX-TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-TRAPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:48:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
elt, = mibBuilder.importSymbols("ELTEX-MIB", "elt")
rldot1dStpTrapVrblVID, rldot1dStpTrapVrblifIndex = mibBuilder.importSymbols("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblVID", "rldot1dStpTrapVrblifIndex")
rndErrorSeverity, rndErrorDesc = mibBuilder.importSymbols("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity", "rndErrorDesc")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, IpAddress, iso, MibIdentifier, NotificationType, Counter64, ModuleIdentity, Unsigned32, TimeTicks, Gauge32, Integer32, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "iso", "MibIdentifier", "NotificationType", "Counter64", "ModuleIdentity", "Unsigned32", "TimeTicks", "Gauge32", "Integer32", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eltNotifications = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 0))
eltNotifications.setRevisions(('2012-07-13 00:00',))
if mibBuilder.loadTexts: eltNotifications.setLastUpdated('201207130000Z')
if mibBuilder.loadTexts: eltNotifications.setOrganization('Eltex Enterprise Co, Ltd.')
i2cBusFailure = NotificationType((1, 3, 6, 1, 4, 1, 35265, 0, 3)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: i2cBusFailure.setStatus('current')
i2cBusOperational = NotificationType((1, 3, 6, 1, 4, 1, 35265, 0, 4)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: i2cBusOperational.setStatus('current')
mibBuilder.exportSymbols("ELTEX-TRAPS-MIB", eltNotifications=eltNotifications, i2cBusOperational=i2cBusOperational, PYSNMP_MODULE_ID=eltNotifications, i2cBusFailure=i2cBusFailure)
