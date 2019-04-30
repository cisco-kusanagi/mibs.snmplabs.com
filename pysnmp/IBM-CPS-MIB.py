#
# PySNMP MIB module IBM-CPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IBM-CPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:39:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Bits, Counter32, iso, ModuleIdentity, ObjectIdentity, NotificationType, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, MibIdentifier, Unsigned32, enterprises, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "Counter32", "iso", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "MibIdentifier", "Unsigned32", "enterprises", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
cps = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 201))
cpsSystemSendTrap = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 201, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpsSystemSendTrap.setStatus('optional')
problemTrap = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 201) + (0,3)).setObjects(("IBM-CPS-MIB", "cpsSystemSendTrap"))
mibBuilder.exportSymbols("IBM-CPS-MIB", problemTrap=problemTrap, ibmProd=ibmProd, cpsSystemSendTrap=cpsSystemSendTrap, ibm=ibm, cps=cps)
