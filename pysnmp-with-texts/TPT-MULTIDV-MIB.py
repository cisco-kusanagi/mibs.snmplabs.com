#
# PySNMP MIB module TPT-MULTIDV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPT-MULTIDV-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:26:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, TimeTicks, IpAddress, MibIdentifier, ObjectIdentity, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, Gauge32, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "TimeTicks", "IpAddress", "MibIdentifier", "ObjectIdentity", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "Gauge32", "Integer32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
policyDVObjs, = mibBuilder.importSymbols("TPT-POLICY-MIB", "policyDVObjs")
tpt_multidv_objs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2)).setLabel("tpt-multidv-objs")
tpt_multidv_objs.setRevisions(('2016-05-25 18:54',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tpt_multidv_objs.setRevisionsDescriptions(('Updated copyright information. Minor MIB syntax fixes.',))
if mibBuilder.loadTexts: tpt_multidv_objs.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_multidv_objs.setOrganization('Trend Micro, Inc.')
if mibBuilder.loadTexts: tpt_multidv_objs.setContactInfo('www.trendmicro.com')
if mibBuilder.loadTexts: tpt_multidv_objs.setDescription("Multiple Digital Vaccine support. Copyright (C) 2016 Trend Micro Incorporated. All Rights Reserved. Trend Micro makes no warranty of any kind with regard to this material, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. Trend Micro shall not be liable for errors contained herein or for incidental or consequential damages in connection with the furnishing, performance, or use of this material. This document contains proprietary information, which is protected by copyright. No part of this document may be photocopied, reproduced, or translated into another language without the prior written consent of Trend Micro. The information is provided 'as is' without warranty of any kind and is subject to change without notice. The only warranties for Trend Micro products and services are set forth in the express warranty statements accompanying such products and services. Nothing herein should be construed as constituting an additional warranty. Trend Micro shall not be liable for technical or editorial errors or omissions contained herein. TippingPoint(R), the TippingPoint logo, and Digital Vaccine(R) are registered trademarks of Trend Micro. All other company and product names may be trademarks of their respective holders. All rights reserved. This document contains confidential information, trade secrets or both, which are the property of Trend Micro. No part of this documentation may be reproduced in any form or by any means or used to make any derivative work (such as translation, transformation, or adaptation) without written permission from Trend Micro or one of its subsidiaries. All other company and product names may be trademarks of their respective holders. ")
class DVIsActive(TextualConvention, Integer32):
    description = 'An indicator of whether a DV is active.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("inactive", 0), ("active", 1))

installedDVTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 1), )
if mibBuilder.loadTexts: installedDVTable.setStatus('current')
if mibBuilder.loadTexts: installedDVTable.setDescription('Table of installed digital vaccine packages.')
installedDVEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 1, 1), ).setIndexNames((0, "TPT-MULTIDV-MIB", "installedDVIndex"))
if mibBuilder.loadTexts: installedDVEntry.setStatus('current')
if mibBuilder.loadTexts: installedDVEntry.setDescription('An entry in the installed DV table. Rows cannot be created or deleted.')
installedDVIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: installedDVIndex.setStatus('current')
if mibBuilder.loadTexts: installedDVIndex.setDescription('Index into the installed DV table, starting with 1.')
installedDVVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: installedDVVersion.setStatus('current')
if mibBuilder.loadTexts: installedDVVersion.setDescription('The installed DV version in string format (major.minor.patch.build).')
installedDVIsActive = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 1, 1, 3), DVIsActive()).setMaxAccess("readonly")
if mibBuilder.loadTexts: installedDVIsActive.setStatus('current')
if mibBuilder.loadTexts: installedDVIsActive.setDescription('Whether this installed DV is active.')
auxiliaryDVTable = MibTable((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2), )
if mibBuilder.loadTexts: auxiliaryDVTable.setStatus('current')
if mibBuilder.loadTexts: auxiliaryDVTable.setDescription('Table of auxiliary digital vaccine packages.')
auxiliaryDVEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2, 1), ).setIndexNames((0, "TPT-MULTIDV-MIB", "auxiliaryDVIndex"))
if mibBuilder.loadTexts: auxiliaryDVEntry.setStatus('current')
if mibBuilder.loadTexts: auxiliaryDVEntry.setDescription('An entry in the auxiliary DV table. Rows cannot be created or deleted.')
auxiliaryDVIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: auxiliaryDVIndex.setStatus('current')
if mibBuilder.loadTexts: auxiliaryDVIndex.setDescription('Index into the auxiliary DV table, starting with 1.')
auxiliaryDVType = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 49))).setMaxAccess("readonly")
if mibBuilder.loadTexts: auxiliaryDVType.setStatus('current')
if mibBuilder.loadTexts: auxiliaryDVType.setDescription('The type of the auxiliary DV.')
auxiliaryDVName = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: auxiliaryDVName.setStatus('current')
if mibBuilder.loadTexts: auxiliaryDVName.setDescription('The name of the auxiliary DV.')
auxiliaryDVVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: auxiliaryDVVersion.setStatus('current')
if mibBuilder.loadTexts: auxiliaryDVVersion.setDescription('The auxiliary DV version number.')
auxiliaryDVPackage = MibTableColumn((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 1, 10, 2, 2, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: auxiliaryDVPackage.setStatus('current')
if mibBuilder.loadTexts: auxiliaryDVPackage.setDescription('The auxiliary DV version in string format (major.minor.patch.build).')
mibBuilder.exportSymbols("TPT-MULTIDV-MIB", PYSNMP_MODULE_ID=tpt_multidv_objs, tpt_multidv_objs=tpt_multidv_objs, auxiliaryDVEntry=auxiliaryDVEntry, auxiliaryDVVersion=auxiliaryDVVersion, installedDVEntry=installedDVEntry, installedDVIsActive=installedDVIsActive, auxiliaryDVType=auxiliaryDVType, installedDVIndex=installedDVIndex, auxiliaryDVName=auxiliaryDVName, auxiliaryDVPackage=auxiliaryDVPackage, auxiliaryDVIndex=auxiliaryDVIndex, auxiliaryDVTable=auxiliaryDVTable, DVIsActive=DVIsActive, installedDVVersion=installedDVVersion, installedDVTable=installedDVTable)
