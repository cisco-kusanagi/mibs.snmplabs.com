#
# PySNMP MIB module PVC-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PVC-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:33:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
atmPortPortIndex, atmPortCardIndex = mibBuilder.importSymbols("CENTILLION-ATMCFG-MIB", "atmPortPortIndex", "atmPortCardIndex")
atmPvcCktId, = mibBuilder.importSymbols("CENTILLION-ATMMON-MIB", "atmPvcCktId")
cnPvcTraps, = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "cnPvcTraps")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Integer32, iso, Bits, Gauge32, Counter32, TimeTicks, NotificationType, ModuleIdentity, IpAddress, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "iso", "Bits", "Gauge32", "Counter32", "TimeTicks", "NotificationType", "ModuleIdentity", "IpAddress", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
remotePvcDown = NotificationType((1, 3, 6, 1, 4, 1, 930, 2, 1, 4, 2) + (0,1)).setObjects(("CENTILLION-ATMCFG-MIB", "atmPortCardIndex"), ("CENTILLION-ATMCFG-MIB", "atmPortPortIndex"), ("CENTILLION-ATMMON-MIB", "atmPvcCktId"))
mibBuilder.exportSymbols("PVC-TRAP-MIB", remotePvcDown=remotePvcDown)
