#
# PySNMP MIB module VMWARE-ESX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VMWARE-ESX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:27:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, Bits, iso, ObjectIdentity, NotificationType, IpAddress, TimeTicks, MibIdentifier, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "Bits", "iso", "ObjectIdentity", "NotificationType", "IpAddress", "TimeTicks", "MibIdentifier", "Counter64", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
vmwProductSpecific, vmwOID = mibBuilder.importSymbols("VMWARE-ROOT-MIB", "vmwProductSpecific", "vmwOID")
oidESX = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 60, 1))
vmwESX = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 1))
esxVMKernel = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 1, 1))
vmkLoaded = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmkLoaded.setStatus('mandatory')
mibBuilder.exportSymbols("VMWARE-ESX-MIB", vmkLoaded=vmkLoaded, esxVMKernel=esxVMKernel, vmwESX=vmwESX, oidESX=oidESX)
