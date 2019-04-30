#
# PySNMP MIB module RAPTOR-SNMPv1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RAPTOR-SNMPv1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:43:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Gauge32, enterprises, Counter64, Bits, Unsigned32, Counter32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, NotificationType, NotificationType, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "enterprises", "Counter64", "Bits", "Unsigned32", "Counter32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "NotificationType", "NotificationType", "iso", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
raptorSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 1294))
raptorModules = MibIdentifier((1, 3, 6, 1, 4, 1, 1294, 1))
raptorObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1294, 2))
raptorTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 1294, 3))
raptorNotifyMessage = MibScalar((1, 3, 6, 1, 4, 1, 1294, 2, 1), OctetString())
if mibBuilder.loadTexts: raptorNotifyMessage.setStatus('mandatory')
raptorNotifyTrap = NotificationType((1, 3, 6, 1, 4, 1, 1294) + (0,1)).setObjects(("RAPTOR-SNMPv1-MIB", "raptorNotifyMessage"))
mibBuilder.exportSymbols("RAPTOR-SNMPv1-MIB", raptorTraps=raptorTraps, raptorNotifyMessage=raptorNotifyMessage, raptorSystems=raptorSystems, raptorModules=raptorModules, raptorNotifyTrap=raptorNotifyTrap, raptorObjects=raptorObjects)
