#
# PySNMP MIB module IBM-CPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IBM-CPS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:50:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, NotificationType, ObjectIdentity, TimeTicks, IpAddress, enterprises, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, NotificationType, Counter64, Gauge32, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "ObjectIdentity", "TimeTicks", "IpAddress", "enterprises", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "NotificationType", "Counter64", "Gauge32", "Integer32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
cps = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 201))
cpsSystemSendTrap = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 201, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpsSystemSendTrap.setStatus('optional')
if mibBuilder.loadTexts: cpsSystemSendTrap.setDescription('This variable contains a textual represenation of all the trap data.')
problemTrap = NotificationType((1, 3, 6, 1, 4, 1, 2, 6, 201) + (0,3)).setObjects(("IBM-CPS-MIB", "cpsSystemSendTrap"))
if mibBuilder.loadTexts: problemTrap.setDescription('This trap is sent whenever a Problem Log Entry is created.')
mibBuilder.exportSymbols("IBM-CPS-MIB", problemTrap=problemTrap, cpsSystemSendTrap=cpsSystemSendTrap, cps=cps, ibm=ibm, ibmProd=ibmProd)
