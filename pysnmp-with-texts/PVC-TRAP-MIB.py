#
# PySNMP MIB module PVC-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PVC-TRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:42:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
atmPortCardIndex, atmPortPortIndex = mibBuilder.importSymbols("CENTILLION-ATMCFG-MIB", "atmPortCardIndex", "atmPortPortIndex")
atmPvcCktId, = mibBuilder.importSymbols("CENTILLION-ATMMON-MIB", "atmPvcCktId")
cnPvcTraps, = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "cnPvcTraps")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, iso, Gauge32, Bits, ObjectIdentity, Integer32, TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, IpAddress, NotificationType, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Gauge32", "Bits", "ObjectIdentity", "Integer32", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "IpAddress", "NotificationType", "Counter32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
remotePvcDown = NotificationType((1, 3, 6, 1, 4, 1, 930, 2, 1, 4, 2) + (0,1)).setObjects(("CENTILLION-ATMCFG-MIB", "atmPortCardIndex"), ("CENTILLION-ATMCFG-MIB", "atmPortPortIndex"), ("CENTILLION-ATMMON-MIB", "atmPvcCktId"))
if mibBuilder.loadTexts: remotePvcDown.setDescription(' This trap is sent when a CLC PVC goes down i.e. the RemotePvcStatus indicator is set to down. atmPortCardIndex.........the ATM card id. atmPortPortIndex.........the ATM port id. atmPvcCktId..............the PVC ckt id.')
mibBuilder.exportSymbols("PVC-TRAP-MIB", remotePvcDown=remotePvcDown)
