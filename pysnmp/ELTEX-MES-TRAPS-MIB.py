#
# PySNMP MIB module ELTEX-MES-TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ELTEX-MES-TRAPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:47:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
rldot1dStpTrapVrblifIndex, rldot1dStpTrapVrblVID = mibBuilder.importSymbols("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblifIndex", "rldot1dStpTrapVrblVID")
rndErrorDesc, rndErrorSeverity = mibBuilder.importSymbols("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc", "rndErrorSeverity")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, ObjectIdentity, Bits, Counter32, IpAddress, Unsigned32, NotificationType, TimeTicks, Integer32, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Bits", "Counter32", "IpAddress", "Unsigned32", "NotificationType", "TimeTicks", "Integer32", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltMesNotifications = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 0))
eltMesNotifications.setRevisions(('2012-07-13 00:00',))
if mibBuilder.loadTexts: eltMesNotifications.setLastUpdated('201207130000Z')
if mibBuilder.loadTexts: eltMesNotifications.setOrganization('Eltex Enterprise Co, Ltd.')
i2cBusFailure = NotificationType((1, 3, 6, 1, 4, 1, 35265, 1, 23, 0, 3)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: i2cBusFailure.setStatus('current')
i2cBusOperational = NotificationType((1, 3, 6, 1, 4, 1, 35265, 1, 23, 0, 4)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: i2cBusOperational.setStatus('current')
transThresholdWarning = NotificationType((1, 3, 6, 1, 4, 1, 35265, 1, 23, 0, 5)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: transThresholdWarning.setStatus('current')
transThresholdOK = NotificationType((1, 3, 6, 1, 4, 1, 35265, 1, 23, 0, 6)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: transThresholdOK.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-TRAPS-MIB", i2cBusOperational=i2cBusOperational, i2cBusFailure=i2cBusFailure, transThresholdOK=transThresholdOK, PYSNMP_MODULE_ID=eltMesNotifications, eltMesNotifications=eltMesNotifications, transThresholdWarning=transThresholdWarning)
